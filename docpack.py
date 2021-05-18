import sys
import shutil
import os
from datetime import date
from pathlib import Path

def zip_folder(folder_path:str, target_name:str):
  p = Path(folder_path)
  zipfile = Path.joinpath(p.parent.absolute(), target_name)
  shutil.make_archive(zipfile, 'zip', folder_path)
  shutil.move(f'{zipfile}.zip', p.absolute())
  print(f'Ergebnis: {zipfile}.zip')

def get_name(value='Archive'):
  v = input(f'Dateiname [{value}]: ')
  if len(v) == 0:
    return value
  return v

def get_version(value='1.0'):
  v = input(f'Version [{value}]: ')
  if len(v) == 0:
    return value
  return v

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Bitte Pfad angeben, der eingepackt werden soll')
    sys.exit(1)
  if not os.path.exists(sys.argv[1]):
    print('Der Pfad existiert leider nicht')
    sys.exit(1)
  
  name = get_name()
  version = get_version()
  d = date.today().strftime('%Y%m%d')
  zip_folder(sys.argv[1], f'{d}_{name}_v{version}' )