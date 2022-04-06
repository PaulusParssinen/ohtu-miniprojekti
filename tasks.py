from invoke import task

@task
def reset_database(ctx):
    ctx.run("python3 src/index.py --reset-database")

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def lint(ctx):
    ctx.run("pylint src --fail-under=7")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def robot(ctx):
    ctx.run("robot src/tests")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task(coverage_report)
def view_report(ctx):
    ctx.run('firefox htmlcov/index.html')
