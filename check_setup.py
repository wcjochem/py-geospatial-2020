import importlib

nm = 'geopandas'

try:
    importlib.import_module(nm)

except ImportError:
    print("Error importing GeoPandas")
    
else:
    try:
        import geopandas
        
        dat = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
        print("Set-up correct!")
    except Exception as e:
        print("Unable to read data file.")
        print(e)
        
