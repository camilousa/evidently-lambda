

def handler(event, context):
    import os
    print("NO PROFILE!")
   # os.environ["AWS_PROFILE"] = "default"
    
    
    
    from evidently.ui.workspace import Workspace
    import pandas as pd
    from evidently import Report
    from evidently.presets import DataDriftPreset
  #  from evidently.presets import *
  #  from evidently.tests import *
    from evidently.ui.workspace import Workspace
    import fsspec
    
    
    
    # Example data
    ref = pd.DataFrame({"feature": [1, 2, 3, 4]})
    cur = pd.DataFrame({"feature": [1.1, 2.2, 3.5, 3.9]})
    
    # Create report
    report = Report(metrics=[DataDriftPreset()])
    my_eval = report.run(reference_data=ref, current_data=cur)
    
    # --- Define workspace in S3 ---
    workspace = Workspace("s3://evidently-132/evidently_workspace/")
    # --- Create or get project ---
    
    project = workspace.create_project("drift_monitoring")
    workspace.add_project(project)
    
    # --- Save report snapshot to S3 ---
    workspace.add_run(project.id, my_eval, include_data=False)
    
    return {
            "statusCode": 200
            }
            

