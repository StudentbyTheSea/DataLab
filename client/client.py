import sys
import json
from collections import defaultdict
from typing import List, Dict
import requests
from utils_datalab import get_info
from utils_datalab import validate_generate_db_metadata
from utils_datalab import generate_db_metadata_from_sdk


class Client:
    def __init__(self,
                 dataset_name_db = None,
                 dataset_name_sdk = None,
                 version = "origin",
                 languages = ['en'],
                 tasks = ['text-classification'],
                 task_categories = ['text-classification'],
                 split = {"train":0, "validation":0, "test":0},
                 transformation = {'type':'origin'},
                 calculate_features = False,
                 field = "text",
                 ):
        self._end_point_add_dataset = "http://datalab.nlpedia.ai:5001/upload_new_dataset"

        self.dataset_name_sdk = dataset_name_sdk
        self.dataset_name_db = dataset_name_db
        self.version = version
        self.languages = languages
        self.tasks = tasks
        self.task_categories = task_categories
        self.split = split
        self.transformation = transformation
        self.calculate_features = calculate_features
        self.field = field

        if dataset_name_db == None:
            raise ValueError(f"the dataset_name_db should not be none:{dataset_name_db}")






    def add_dataset_metadata(self):

        metadata_db = validate_generate_db_metadata(dataset_name = self.dataset_name_db,
                                      transformation = self.transformation,
                                      version = self.version,
                                      task_categories = self.task_categories,
                                      tasks = self.tasks,
                                      split = self.split,
                                      languages = self.languages)

        samples = [
            {"split_name": "train",
             "features": {
             },
             }
        ]
        data_json = {
            'metadata': metadata_db,
            'samples': samples
        }



        response = requests.post(self._end_point_add_dataset, json=data_json)
        if response.status_code != 200:
            raise ConnectionError(f"[Error on metric: {rjson['metric']}]\n[Error Message]: {rjson['message']}")

        print(response.status_code)


    def add_dataset_from_sdk(self):


        # get metadata and dataset information from sdk by passing the dataset name of the sdk
        metadata_sdk, metadata_features_sdk, dataset_sdk = get_info(self.dataset_name_sdk,
                                                                    calculate_features= self.calculate_features,
                                                                    field = self.field)

        # reformat the metadata information for db
        metadata_db = generate_db_metadata_from_sdk(metadata=metadata_sdk,
                                                           features=metadata_features_sdk,
                                                           dataset_name_db=self.dataset_name_db,
                                                           transformation= self.transformation,
                                                           version = self.version,
                                                           languages=self.languages, )

        # reformat the sample information for db
        MAX_NUMBER_OF_SAMPLES = 20000
        samples_db = []
        for split in dataset_sdk.keys():
            for idx, sample in enumerate(dataset_sdk[split]):
                if idx > MAX_NUMBER_OF_SAMPLES:
                    break
                samples_db.append({
                    'split_name': split,
                    'features': sample
                })

        # prepare the data to be uploaded
        data_json = {
            'metadata': metadata_db,
            'samples': samples_db
        }


        response = requests.post(self._end_point_add_dataset, json=data_json)
        if response.status_code != 200:
            raise ConnectionError(f"[Error on metric: {rjson['metric']}]\n[Error Message]: {rjson['message']}")

        print(response.status_code)


# Example 1
# client = Client(dataset_name_db="test_pf1")
# client.add_dataset_metadata()


# Example 2
client = Client(dataset_name_db="test_pf7", dataset_name_sdk="mr", calculate_features = True, field = "text")
client.add_dataset_from_sdk()


# Example 3
# client = Client(dataset_name_db="test_pf5", dataset_name_sdk="xsum", calculate_features = False)
# client.add_dataset_from_sdk()