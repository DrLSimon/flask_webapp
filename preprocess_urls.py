
import requests
import pickle
import numpy as np
from tqdm import tqdm

def url_checker(url):
    try:
        #Get Url
        get = requests.get(url, timeout=0.1)
        # if the request succeeds 
        if get.status_code == 200:
            return True
        else:
            return False

    #Exception
    except requests.exceptions.RequestException as e:
        return False


def main():
    with open('url_comps_rep_fp.pkl', 'rb') as file:
        comps = pickle.load(file)
    print('start', len(comps))
    comps = [np.unique(comp) for comp in comps]
    print(1)
    comps = [[url for url in comp if url_checker(url)] for comp in tqdm(comps)]
    print(2)
    with open( "filtered_url_comps_rep_fp.pkl", "wb" ) as ofile:
        pickle.dump(comps, ofile)
    print('done', len(comps))

    
    

if __name__=='__main__':
    main()
