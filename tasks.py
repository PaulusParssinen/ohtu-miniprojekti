from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def robot(ctx):
    ctx.run("robot src/tests")

@task
def build(ctx):
    ctx.run("python3 src/initialize_db.py")
