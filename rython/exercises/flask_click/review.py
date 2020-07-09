import click

@click.command()
@click.option("--film-name", prompt="Film name")
@click.option("--stars", prompt="How many stars?")
def saveReview(film_name, stars):
    f = open("file/file1.txt", 'a')
    f.write(film_name + ', ' + stars + '\n')

saveReview()