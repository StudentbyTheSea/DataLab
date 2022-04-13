# coding=utf-8
# Copyright 2022 The HuggingFace datasets Authors, DataLab Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""XL-Sum abstractive summarization dataset."""
import os
import datalabs
from datalabs.tasks import TextClassification


_CITATION = """\
@misc{yang2022cino,
      title={CINO: A Chinese Minority Pre-trained Language Model}, 
      author={Ziqing Yang and Zihang Xu and Yiming Cui and Baoxin Wang and Min Lin and Dayong Wu and Zhigang Chen},
      year={2022},
      eprint={2202.13558},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
}
"""
_DESCRIPTION = """\
WCM is based on the data from Wikipedia. It covers seven languages including Mongolian, Tibetan,
Uyghur, Kazakh, Korean, Cantonese and Standard Chinese. Dataset collect the Wikipedia
page dumps and the Wikipedia category dumps of the languages in question. The purpose of
WCM is to evaluate the zero-shot cross-lingual ability of MPLMs on the Chinese minority languages.
By referring to the category system of Chinese Wikipedia, WCM is divided to 10 categories for the classification task: Art, Geography,
History, Nature, Science, Personage, Technology, Education, Economy and Health.

WCM-v2 adjusts the number of samples in each category and language, and the distribution is relatively more balanced.

For more information, please refer to https://arxiv.org/pdf/2202.13558.pdf 

"""
_HOMEPAGE = "https://github.com/ymcui/Chinese-Minority-PLM"
_TRAIN_DOWNLOAD_URL = "https://drive.google.com/u/0/uc?id=1ZI9LbYmEHekG71pjdK9uoajC-L47Zugn&export=download"
_VALIDATION_DOWNLOAD_URL = "https://drive.google.com/u/0/uc?id=1dteUEgN361x66Of5w-cZc8dae5h1dnyH&export=download"

_TEST_DOWNLOAD_URL = {
    "bo": "https://drive.google.com/uc?export=download&id=1ASxhqJimAsf5cmK-5tg2fOqYAMPB5Ks_",
    "kk": "https://drive.google.com/uc?export=download&id=1Icor-kWxcNKGXs5hvSghw0F4w7BM06sf",
    "ko": "https://drive.google.com/uc?export=download&id=1xF3PWsA4C4qtleKBlx0Fsta2GJhu2m4k",
    "mn": "https://drive.google.com/uc?export=download&id=1V6HlNI66lp_aMtyxRkiBjpuHHE-DG5WA",
    "ug": "https://drive.google.com/uc?export=download&id=11Ah9x247Bf8Pr2DOwnwFMJJAatIYtJ8X",
    "yue": "https://drive.google.com/uc?export=download&id=1mSki_4-RXtWO8B3hvwiOIS5pAudTsQVP",
    "zh": "https://drive.google.com/uc?export=download&id=1N_CKb2mHkdjyCr7XCFP8V8RR-XvvYw0_",
}

_LANGUAGES = ["zh","yue","bo","mn","ug","kk","ko"]

class WCM_v2Config(datalabs.BuilderConfig):
    def __init__(self, data_url, **kwargs):
        """BuilderConfig for MLQA
        Args:
          data_url: `string`, url to the dataset
          **kwargs: keyword arguments forwarded to super.
        """
        def __init__(self, **kwargs):
            """
            Args:
                **kwargs: keyword arguments forwarded to super.
            """
            super(wcmConfig, self).__init__(version=datalabs.Version("2.0.0", ""), **kwargs)

class WCM_v2(datalabs.GeneratorBasedBuilder):
    VERSION = datalabs.Version("2.0.0")

    BUILDER_CONFIGS = [
        datalabs.BuilderConfig(
            name="{}".format(lang),
            version=datalabs.Version("2.0.0")
        )
        for lang in _LANGUAGES
    ]

    def _info(self):
        return datalabs.DatasetInfo(
            description=_DESCRIPTION,
            features=datalabs.Features(
                {
                    "text": datalabs.Value("string"),
                    "label": datalabs.features.ClassLabel(names=["Art", "Geography"，"History","Nature", "Science", "Personage", "Technology",
                                                                 "Education", "Economy","Health"]),
                }
            ),
            supervised_keys=None,
            homepage=_HOMEPAGE,
            citation=_CITATION,
            version=self.VERSION,
            #topic
            task_templates=[TextClassification(text_column="text", label_column="label", task="text-classification")],
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        lang = str(self.config.name)
        #url = _URL.format(lang, self.VERSION.version_str[:-2])
        
        train_path = dl_manager.download_and_extract(_TRAIN_DOWNLOAD_URL)
        print(f"train_path: \t{train_path}")
        validation_path = dl_manager.download_and_extract(_VALIDATION_DOWNLOAD_URL)
        print(f"validation_path: \t{validation_path}")
        test_path = dl_manager.download_and_extract(_TEST_DOWNLOAD_URL[lang])
        print(f"test_path: \t{test_path}")
    
        return [
            datalabs.SplitGenerator(
                name=datalabs.Split.TRAIN,
                gen_kwargs={
                    "filepath": train_path,
                },
            ),
            datalabs.SplitGenerator(
                name=datalabs.Split.VALIDATION,
                gen_kwargs={
                    "filepath": validation_path,
                },
                
            datalabs.SplitGenerator(
                name=datalabs.Split.TEST,
                gen_kwargs={
                    "filepath": test_path,
                },
            ),

            ),
        ]
    #txt
    def _generate_examples(self, filepath):
        """Yields examples as (key, example) tuples."""
        with open(filepath, encoding="utf-8") as f:
            for idx_, row in enumerate(f):     
                yield idx_, {
                    row
                }
