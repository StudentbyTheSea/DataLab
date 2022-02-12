# coding=utf-8
# Copyright 2022 DataLab Authors and the current dataset script contributor.
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

"""Text Classification dataset."""

import csv

import datalabs
from datalabs.tasks import TextClassification
from featurize.general import get_features_sample_level
from aggregate.general import get_features_dataset_level
from datalabs.utils.more_features import prefix_dict_key, get_feature_arguments
from datalabs import PLMType, SettingType

_DESCRIPTION = """\
 Movie-review data for use in sentiment-analysis experiments. Available are collections 
 of movie-review documents labeled with respect to their overall sentiment polarity (positive or negative)
  or subjective rating (e.g., "two and a half stars")
"""

_CITATION = """\
@inproceedings{pang-lee-2005-seeing,
    title = "Seeing Stars: Exploiting Class Relationships for Sentiment Categorization with Respect to Rating Scales",
    author = "Pang, Bo  and
      Lee, Lillian",
    booktitle = "Proceedings of the 43rd Annual Meeting of the Association for Computational Linguistics ({ACL}{'}05)",
    month = jun,
    year = "2005",
    address = "Ann Arbor, Michigan",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P05-1015",
    doi = "10.3115/1219840.1219855",
    pages = "115--124",
}
"""

"""
if your link is from google drive, you just need to modify following template by replacing XXXXX with real string
https://drive.google.com/uc?id=XXXXX=download

You can get "XXXXX" from the link of `sharing to any`, for example, we can know
XXXXX = 1t-2aRCGru5yJzpJ-o4uB6UmHbNRzNfIb
from 
https://drive.google.com/file/d/1t-2aRCGru5yJzpJ-o4uB6UmHbNRzNfIb/view?usp=sharing



"""
_TRAIN_DOWNLOAD_URL = "https://drive.google.com/uc?id=1FCqdCBYNahOmoMOW7L29EZGanJKksgwT&export=download"
_TEST_DOWNLOAD_URL = "https://drive.google.com/uc?id=1t-2aRCGru5yJzpJ-o4uB6UmHbNRzNfIb&export=download"



# def prefix_dict_key(dict_obj, prefix):
#     dict_obj_new = {}
#     for k, v in dict_obj.items():
#         dict_obj_new[prefix + "_" + k] = v
#     return dict_obj_new
#
#
#
# def get_feature_arguments(dict_output, field = "text", feature_level = "sample_level"):
#     """Automate following code based on the output of `get_features_sample_level`
#      additional_features = datalabs.Features(
#         {
#             TEXT+ "_" + "length": datalabs.Value(dtype="int64",
#                                      is_bucket=True,
#                                      ),
#         }
#     )
#     """
#     dict_feature_argument = {}
#     for func_name, func_value in dict_output.items():
#         key = field + "_" + func_name
#         value = "int64"
#         is_bucket = True
#         if isinstance(func_value, int):
#             value = "int64"
#             is_bucket = True
#         elif isinstance(func_value, str):
#             value = "string"
#             is_bucket = True
#         elif isinstance(func_value, dict):
#             value = "dict"
#             is_bucket = False
#
#         if feature_level == "dataset_level":
#             is_bucket = False
#         dict_feature_argument[key] = datalabs.Value(dtype=value, is_bucket=is_bucket, feature_level = feature_level, raw_feature = False)
#
#     return dict_feature_argument



EXPAND = True
FIELD = "text"

class MR(datalabs.GeneratorBasedBuilder):
    """Movie Review Dataset."""

    def _info(self):

        features_dataset = {}
        features_sample = datalabs.Features(
                {
                     FIELD: datalabs.Value("string"),
                    "label": datalabs.features.ClassLabel(names=["positive", "negative"]),
                }
            )

        if EXPAND:

            # dict_feature_argument = {}
            # for func_name, func_value in get_features_sample_level("").items():
            #     key = TEXT + "_" + func_name
            #     value = "int64"
            #     is_bucket = True
            #     if isinstance(func_value,int):
            #         value = "int64"
            #         is_bucket = True
            #     elif isinstance(func_value,str):
            #         value = "string"
            #         is_bucket = True
            #     elif isinstance(func_value,dict):
            #         value = "dict"
            #         is_bucket = False
            #
            #     dict_feature_argument[key] = datalabs.Value(dtype=value, is_bucket=is_bucket, feature_level="sample_level")

            dict_feature_argument = get_feature_arguments(get_features_sample_level(""), field=FIELD, feature_level="sample_level")
            additional_features = datalabs.Features(dict_feature_argument)
            features_sample.update(additional_features)




            dict_feature_argument = get_feature_arguments(get_features_dataset_level([""]), field=FIELD, feature_level="dataset_level")
            features_dataset = datalabs.Features(dict_feature_argument)

            # features_dataset= datalabs.Features(
            #     {
            #         TEXT+ "_" + "avg_length": datalabs.Value(dtype="int64",
            #                                  is_bucket=False,
            #                                  ),
            #     }
            # )

        # class Prompt:
        #     language: str = "en"
        #     description: str = "prompt description"
        #     template: str = None
        #     answers: dict = None
        #     supported_plms: List[str] = None
        #     results: List[PromptResult] = None

        return datalabs.DatasetInfo(
            description=_DESCRIPTION,
            features=features_sample,
            features_dataset=features_dataset,
            homepage="http://www.cs.cornell.edu/people/pabo/movie-review-data/",
            citation=_CITATION,
            task_templates=[TextClassification(text_column=FIELD, label_column="label", task="sentiment-classification")],
            prompts=[datalabs.Prompt(template="{text}, Overall it is a [mask] movie.",
                                     answers={"0":"positive","1":"negative"},
                                     supported_plm_types=[PLMType.masked_language_model]),
                     datalabs.Prompt(template="{text}, Overall it is a [mask] movie.",
                                     answers={"0": "positive", "1": "negative"},
                                     supported_plm_types=[PLMType.masked_language_model]),
                     ]
        )




    def _split_generators(self, dl_manager):
        train_path = dl_manager.download_and_extract(_TRAIN_DOWNLOAD_URL)
        print(f"train_path: \t{train_path}")
        test_path = dl_manager.download_and_extract(_TEST_DOWNLOAD_URL)
        return [
            datalabs.SplitGenerator(name=datalabs.Split.TRAIN, gen_kwargs={"filepath": train_path}),
            datalabs.SplitGenerator(name=datalabs.Split.TEST, gen_kwargs={"filepath": test_path}),
        ]

    def _generate_examples(self, filepath):
        """Generate dataset examples."""

        textualize_label = {"0": "negative",
                            "1": "positive"}

        with open(filepath, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            for id_, row in enumerate(csv_reader):
                text, label = row[0], row[1]

                label = textualize_label[label]
                text = text

                raw_feature_info = {FIELD: text, "label": label}

                if not EXPAND:
                    yield id_, raw_feature_info
                else:
                    additional_feature_info = prefix_dict_key(get_features_sample_level(text), FIELD)

                    # additional_feature_info_modify = {}
                    # for k, v in additional_feature_info.items():
                    #     additional_feature_info_modify[FIELD + "_" + k] = v

                    raw_feature_info.update(additional_feature_info)
                    yield id_, raw_feature_info

