import pandas as pd

from relbench.base import Database, Dataset, Table


class EnergyDataset(Dataset):

    def make_db(self) -> Database:
        r"""Process the raw files into a database."""
        local_file = "/lfs/local/0/fengyuli/relbench/relbench/datasets/energy.xlsx"

        all_entities = pd.read_excel(local_file, sheet_name="All Entities")
        entity_ownership = pd.read_excel(local_file, sheet_name="Entity Ownership")
        coal_plant_ownership = pd.read_excel(
            local_file, sheet_name="Coal Plant Ownership"
        )
        gas_pipeline_ownership = pd.read_excel(
            local_file, sheet_name="Gas Pipeline Ownership"
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
        tables["all_entities"] = Table(
            df=all_entities, fkey_col_to_pkey_table={}, pkey_col="Entity ID"
        )
        tables["entity_ownership"] = Table(
            df=entity_ownership, fkey_col_to_pkey_table={}, pkey_col="Subject Entity ID"
        )
        tables["coal_plant_ownership"] = Table(
            df=coal_plant_ownership,
            fkey_col_to_pkey_table={"Owner GEM Entity ID": "all_entities"},
        )
        tables["gas_pipeline_ownership"] = Table(
            df=gas_pipeline_ownership,
            fkey_col_to_pkey_table={"Owner GEM Entity ID": "all_entities"},
        )
        tables["bioenergy_power_ownership"] = Table(
            df=bioenergy_power_ownership,
            fkey_col_to_pkey_table={"Owner GEM Entity ID": "all_entities"},
        )
        tables["coal_mine_ownership"] = Table(
            df=coal_mine_ownership,
            fkey_col_to_pkey_table={"Owner GEM Entity ID": "all_entities"},
        )
        tables["iron_min_ownership"] = Table(
            df=iron_min_ownership,
            fkey_col_to_pkey_table={"Owner GEM Entity ID": "all_entities"},
        )
        tables["gas_pipeline_ownership"] = Table(
            df=gas_pipeline_ownership,
            fkey_col_to_pkey_table={"Owner GEM Entity ID": "all_entities"},
        )
        tables["steel_plant_ownership"] = Table(
            df=steel_plant_ownership,
            fkey_col_to_pkey_table={"Owner GEM Entity ID": "all_entities"},
        )
        return Database(tables)


if __name__ == "__main__":
    dataset = EnergyDataset()
    db = dataset.make_db()
