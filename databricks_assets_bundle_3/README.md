>> conda activate jobs

>> pip install databricks-cli

[>] Checking the version
>> databricks -v

[>] Only Databricks CLI 0.205.0 it work it
[>] WinGet installation for Windows
[>] For this installation option, you use winget to automatically download and install the latest Databricks CLI executable release.
[>] From your Command Prompt, run the following two winget commands to install the CLI, and then restart your Command Prompt:
[>] Bash
>> winget search databricks
>> winget install Databricks.DatabricksCLI

[>] Deleting profile
>> C:\Users\Lenovo\.databrickscfg
; The profile defined in the DEFAULT section is to be used as a fallback when no profile is explicitly specified.
[DEFAULT]
host  = https://adb-6523536500265509.9.azuredatabricks.net
token = dapi89b696451baee2c72b5250293a479f2d

[meu-perfil]
host      = https://dbc-636f7eed-7ad3.cloud.databricks.com
auth_type = databricks-cli

[yuan-perfil]
host      = https://dbc-346fb32e-aa93.cloud.databricks.com
auth_type = databricks-cli

[cni]
host      = https://adb-6523536500265509.9.azuredatabricks.net
auth_type = databricks-cli

[>] Accessing
databricks auth login --profile databricks_asset
v Databricks host (e.g. https://<databricks-instance>.cloud.databricks.com): https://dbc-2288932a-12a3.cloud.databricks.com

or 

databricks configure --token --host https://dbc-2288932a-12a3.cloud.databricks.com


databricks workspace list /Users --profile databricks_asset

[>] Get the list of users on workspace
>> databricks workspace list /Users --profile databricks_asset



[>] To get clusters list
>> databricks clusters list


[>] Running databricks assets
>> databricks bundle validate
>> databricks bundle deploy -t dev/ development
>> databricks bundle run -t dev example_job
>> databricks bundle deploy -t dev
>> databricks bundle run -t dev job_orquestrado


# TARGETS: Define diferentes ambientes (dev, prod, etc.)
targets:
  dev:                      # Nome do ambiente de desenvolvimento
    mode: development       # Modo de desenvolvimento (habilita certas funcionalidades)

    # RESOURCES: Define recursos Databricks (jobs, clusters, pipelines, etc.)
    resources:
      # JOBS: Seção para definir trabalhos/pipelines
      jobs:
        job_orquestrado:    # Nome interno do job
          # Nome que aparece na interface do Databricks
          # Resultado: "Job Pipeline Orquestrado - databricks (dev)"
          name: Job Pipeline Orquestrado - ${bundle.name} (${bundle.target})


databricks bundle deploy -t dev
databricks bundle run -t dev job_orquestrado