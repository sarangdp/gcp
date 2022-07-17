1. First, back in Cloud Shell, export the name of your Cloud project as an environment variable. Replace <your_project_name> with the GCP Project ID found in the 
   CONNECTION DETAILS section of the lab.

    * `export PROJECT=<your_project_name>`
    
 2. Then run the following commands from Cloud Shell to create a service account:
 
     * `gcloud iam service-accounts create my-account --display-name my-account`
     * `gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:my-account@$PROJECT.iam.gserviceaccount.com --role=roles/bigquery.admin`
     * `gcloud iam service-accounts keys create key.json --iam-account=my-account@$PROJECT.iam.gserviceaccount.com`
     * `export GOOGLE_APPLICATION_CREDENTIALS=key.json`
