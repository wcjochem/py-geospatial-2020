import importlib

nm = 'geopandas'

try:
    importlib.import_module(nm)

except ImportError:
    print("Error importing GeoPandas")
    
else:
    try:
        import geopandas
        
        dat = geopandas.read_file()
        print("Set-up correct!")
    else Exception as e:
        print("Unable to read data file.")
        print(e)
        
