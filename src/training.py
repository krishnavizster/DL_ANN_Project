from src.utils.common import read_config
from src.utils.data_mgmt import get_data_
import argparse


def training_(config_path):
    config = read_config(config_path)

    validation_datasize = config["params"]["validation_datasize"]
    get_data()
    

    print(config)

if __name__ == '__main__':
    args =argparse.ArgumentParser()

    args.add_argument('--config',"-c",default="config.yaml")

    parsed_args=args.parse_args()

    training(config_path=parsed_args.config) 
