import os
import shutil
from pathlib import Path

import pandas as pd

from relbench.base import Database, Dataset, Table
from relbench.utils import decompress_gz_file


class EnergyDataset(Dataset):

    def make_db(self) -> Database:
        r"""Process the raw files into a database."""
        local_file = "/lfs/local/0/fengyuli/relbench/relbench/datasets/energy.xlsx"

        all_entities = pd.read_excel(local_file, sheet_name="All Entities")
        entity_ownership = pd.read_excel(local_file, sheet_name="Entity Ownership")
        coal_plant_ownership = pd.read_excel(
            local_file, sheet_name="Coal Plant Ownership"
        )
        bioenergy_power_ownership = pd.read_excel(
            local_file, sheet_name="Bioenergy Power Ownership"
        )
        coal_mine_ownership = pd.read_excel(
            local_file, sheet_name="Coal Mine Ownership"
        )
        iron_min_ownership = pd.read_excel(local_file, sheet_name="Iron Mine Ownership")
        gas_pipeline_ownership = pd.read_excel(
            local_file, sheet_name="Gas Pipeline Ownership"
        )
        steel_plant_ownership = pd.read_excel(
            local_file, sheet_name="Steel Plant Ownership"
        )

        tables = {}
        tables["all_entities"] = Table(df=all_entities, pkey_col="Entity ID")


if __name__ == "__main__":
    dataset = EnergyDataset()
    db = dataset.make_db()
