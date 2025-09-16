>> conda activate jobs

>> pip install databricks-cli

>> Checking the version
>> databricks -v

>> Only Databricks CLI 0.205.0 it work it
>> WinGet installation for Windows
For this installation option, you use winget to automatically download and install the latest Databricks CLI executable release.
From your Command Prompt, run the following two winget commands to install the CLI, and then restart your Command Prompt:
Bash
winget search databricks
winget install Databricks.DatabricksCLI

>> Deleting profile
>> C:\Users\Lenovo\.databrickscfg
; The profile defined in the DEFAULT section is to be used as a fallback when no profile is explicitly specified.
[DEFAULT]
host  = https://adb-6523536500265509.9.azuredatabricks.net
token = TOKEN

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
>> databricks auth login --profile databricks_asset
>> v Databricks host (e.g. https://<databricks-instance>.cloud.databricks.com): https://dbc-2288932a-12a3.cloud.databricks.com

>> databricks workspace list /Users --profile databricks_asset

>> Get the list of users on workspace
>> databricks workspace list /Users --profile databricks_asset


[>] To get clusters list
>> databricks clusters list

[>] Running databricks assets
>> databricks bundle validate
>> databricks bundle deploy -t dev/ development
>> databricks bundle run -t dev example_job
>> databricks bundle run -t development job_orquestrado





TOKEN

databricks configure --delete --profile DEFAULT
databricks configure --delete --profile <profile-name>

# dapi317ff443414b9aae665b9195224913b4

Name         Host                                                Valid
DEFAULT      https://adb-6523536500265509.9.azuredatabricks.net  NO
meu-perfil   https://dbc-636f7eed-7ad3.cloud.databricks.com      NO
yuan-perfil  https://dbc-346fb32e-aa93.cloud.databricks.com      NO
cni          https://adb-6523536500265509.9.azuredatabricks.net  NO



databricks configure --token --host https://dbc-2288932a-12a3.cloud.databricks.com


# ===============================
# Databricks Asset Bundle Config
# ===============================

bundle:
  # Nome do bundle (pacote de recursos que será deployado)
  name: my_first_bundle

workspace:
  # URL do workspace Databricks
  host: https://dbc-2288932a-12a3.cloud.databricks.com

resources:
  # Lista de recursos que serão deployados no workspace
  jobs:
    # Definição de um job
    example_job:
      # Nome do job que aparecerá no Databricks Jobs UI
      name: "Example Job from Bundle"
      # Lista de tasks (notebooks/scripts) que o job irá executar
      tasks:
        - task_key: run_example_notebook
          # Chave única da task dentro do job
          notebook_task:
            # Caminho do notebook dentro do workspace
            notebook_path: /Users/zhang489yuan@gmail.com/testing
          #compute:
          #  service:
          # Em serverless-only workspace, não precisa declarar cluster/compute
          # O Databricks automaticamente usa serverless compute

# ===============================
# Targets (Ambientes)
# ===============================
targets:
  dev:
    # Ambiente de desenvolvimento
    workspace:
      # URL do workspace (pode ser diferente do bundle global se necessário)
      host: https://dbc-2288932a-12a3.cloud.databricks.com
      # Diretório onde os arquivos do bundle serão copiados dentro do workspace
      root_path: /Users/zhang489yuan@gmail.com/.bundle/my_first_bundle/dev
    # Define que este target será usado por padrão no CLI
    default: true

# ===============================
# Observações:
# - O job "example_job" irá executar o notebook especificado
# - Em workspaces serverless, não é necessário criar clusters
# - Múltiplas tasks podem ser adicionadas dentro de "tasks"
# - Múltiplos targets podem ser definidos (dev, staging, prod)
# - Para deploy e execução:
#     databricks bundle validate
#     databricks bundle deploy -t dev
#     databricks bundle run -t dev example_job
# ===============================





# =====================================================
# Databricks Asset Bundle - Configuração com comentários
# =====================================================

# ----------------------------------------
# Nome único do bundle (identificador lógico do projeto)
# ----------------------------------------
bundle:
  name: databricks_bundle_staging
  # Este é o nome do bundle e será usado para organizar paths e jobs.

# ----------------------------------------
# Configuração do workspace do Databricks
# ----------------------------------------
workspace:
  host: https://dbc-2288932a-12a3.cloud.databricks.com
  # URL do workspace no Azure Databricks
  root_path: /Workspace/Users/zhang489yuan@gmail.com/bundles/${bundle.name}/${bundle.target}
  # Caminho base onde os artefatos do bundle serão sincronizados.
  # ${bundle.name} → "databricks_bundle_staging"
  # ${bundle.target} → "development" ou outro target definido abaixo

# ----------------------------------------
# Artefatos do bundle (notebooks ou scripts locais)
# ----------------------------------------
artifacts:
  main_notebook:
    type: notebook
    # Tipo de artefato: notebook Databricks
    path: /Workspace/Users/zhang489yuan@gmail.com/Bundleno_Databricks/main
    # Caminho dentro do workspace onde o notebook será colocado
    files:
      - source: src/main.py
        # Arquivo local que será sincronizado com o workspace

  process_notebook:
    type: notebook
    path: /Workspace/Users/zhang489yuan@gmail.com/Bundleno_Databricks/process
    files:
      - source: src/process.py
        # Arquivo local do segundo notebook

# ----------------------------------------
# Definição de ambientes (targets)
# ----------------------------------------
targets:
  development:
    mode: development
    # Modo "development" permite sincronização automática dos notebooks

    # Recursos que serão criados neste target
    resources:
      jobs:
        job_orquestrado:
          name: Job Pipeline Orquestrado - ${bundle.name} (${bundle.target})
          # Nome do job no Databricks, usando variáveis do bundle e target

          # Configuração de notificações por e-mail
          email_notifications:
            on_success:
              - zhang489yuan@gmail.com
            on_failure:
              - data-team@suaempresa.com

          # Lista de tasks (tarefas) do job
          tasks:
            # ----------------------------
            # Primeira tarefa do pipeline
            # ----------------------------
            - task_key: tarefa_main
              # Identificador único da task
              notebook_task:
                notebook_path: ${workspace.root_path}/main
                # Notebook que será executado
              existing_cluster_id: 1126-202621-niece981
              # Cluster existente usado para execução

              # Bibliotecas específicas para esta task
              libraries:
                - pypi:
                    package: pandas==2.2.1
                - pypi:
                    package: requests
                - whl: dbfs:/my-wheels/meu_pacote-0.1.0-py3-none-any.whl
                # Permite instalar pacotes PyPI ou arquivos .whl customizados

            # ----------------------------
            # Segunda tarefa: depende da primeira
            # ----------------------------
            - task_key: tarefa_process
              depends_on:
                - task_key: tarefa_main
                # Esta task só executa após a tarefa_main
              notebook_task:
                notebook_path: ${workspace.root_path}/process
              existing_cluster_id: 1126-202621-niece981
              # Reutiliza o mesmo cluster da primeira task

              libraries:
                - pypi:
                    package: pandas==2.2.1
                # Pode definir bibliotecas diferentes se necessário

              # Opção comentada: criar um novo cluster dedicado para a task
              # new_cluster:
              #   spark_version: 13.3.x-scala2.12
              #   node_type_id: Standard_DS3_v2
              #   driver_node_type_id: Standard_DS3_v2
              #   autoscale:
              #     min_workers: 1
              #     max_workers: 4
              #   data_security_mode: NONE
              #   custom_tags:
              #     ResourceClass: Standard
              # Caso queira um cluster novo em vez de usar um existente

# =====================================================
# Observações finais:
# - ${bundle.name}, ${bundle.target}, ${workspace.root_path} → variáveis dinâmicas
# - Cada task pode ter dependências, clusters e bibliotecas específicas
# - É possível adicionar mais notebooks/artifacts e targets
# - O bundle organiza jobs e artefatos de forma consistente para desenvolvimento e produção
# =====================================================
