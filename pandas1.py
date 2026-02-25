import kagglehub

# Download latest version
path = kagglehub.dataset_download("yusufdelikkaya/online-sales-dataset")

print("Path to dataset files:", path)