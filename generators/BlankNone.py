import yaml
from yaml.representer import Representer
from yaml.dumper import Dumper

def getExcelSheetValue(excel, config):
  v = excel[config["sheet"]][config["p"]].value
  
  if v == "" or not v:
    v = config["defaultValue"]

  return v

class BlankNone(Representer):
  """Print None as blank when used as context manager"""
  def represent_none(self, *_):
    return self.represent_scalar(u'tag:yaml.org,2002:null', u'')

  def __enter__(self):
    self.prior = Dumper.yaml_representers[type(None)]
    yaml.add_representer(type(None), self.represent_none)

  def __exit__(self, exc_type, exc_val, exc_tb):
    Dumper.yaml_representers[type(None)] = self.prior