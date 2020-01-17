import random

def primary():
 # print("Keep it logically awesome.")

 f = open("quotes.txt")
 quotes = f.readlines()
 f.close()

 last = len(quotes)-1

 rnd = random.randint(0, last)
 print(quotes[rnd].rstrip('\n'))

 rnd = random.randint(0, last)
 print(quotes[rnd], end='')

 data = 'some data to be written to the file'
 f = open("quotes.txt", "a")
 f.write(data)
 f.close()

if __name__== "__main__":
  primary()
