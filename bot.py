from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC

def translatefromgoogle(phrase):
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=" + str(phrase))
    translated = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span").text
    return translated

client = commands.Bot(command_prefix="._")

@client.event
async def on_ready():
    print ("Ready.")

@client.command()
async def translate(ctx,*,arg):
    translated = translatefromgoogle(arg)
    if (len > 1000):
        with open('translation.txt','w+') as fp:
            fp.write(translated)
        with open('translation.txt','r') as f:
            await ctx.send(file=discord.File(f,"translation.txt"))
    else:
        await ctx.send(translated)


client.run("TOKEN GOES HERE")