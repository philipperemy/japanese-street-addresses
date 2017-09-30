import json
import logging
from glob import glob

from new_scrape import change_ip
from new_scrape import run_scrape


def run():
    files = glob('regions/*.json')
    for json_file in files:
        with open(json_file, 'rb') as j:
            data = json.load(j)
            for region_name, region_data in data.items():
                print(region_name)
                urls = region_data['sub_region']['level_2']
                urls = sorted(list(set(urls)))  # make sure no redundancy.
                for i, url in enumerate(urls):
                    if i % 10 == 0:
                        logging.info('IP SWITCHING.')
                        change_ip()  # we do not want to fire all our IPs. So lets switch from time to time.
                    logging.info('({1}/{2}) MAIN - REQUESTING {0}'.format(url, i, len(urls)))
                    run_scrape(url)


if __name__ == '__main__':
    run()
