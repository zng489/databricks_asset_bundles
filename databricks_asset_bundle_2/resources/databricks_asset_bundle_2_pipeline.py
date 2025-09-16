from databricks.bundles.pipelines import Pipeline

databricks_asset_bundle_2_pipeline = Pipeline.from_dict(
    {
        "name": "databricks_asset_bundle_2_pipeline",
        "target": "databricks_asset_bundle_2_${bundle.target}",
        "catalog": "workspace",
        "libraries": [
            {
                "notebook": {
                    "path": "src/dlt_pipeline.ipynb",
                },
            },
        ],
        "configuration": {
            "bundle.sourcePath": "${workspace.file_path}/src",
        },
    }
)
