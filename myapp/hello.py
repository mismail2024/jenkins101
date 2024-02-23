import fire

def hello(name="World"):
  return "From Jenkins app file, Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
  
