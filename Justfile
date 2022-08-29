set dotenv-load

version level:
    git diff-index --exit-code HEAD > /dev/null || ! echo You have untracked changes. Commit your changes before bumping the version.
    toml set -i pyproject.toml project.version $(semver bump {{level}} $(toml get -r pyproject.toml project.version))
    VERSION=$(toml get pyproject.toml project.version -r) && \
        git commit -am "Bump version {{level}} to $VERSION" && \
        git tag v$VERSION && \
        git push origin v$VERSION
    git push

publish:
   FLIT_USERNAME="__token__" \
   FLIT_PASSWORD=$PYPI_API_TOKEN \
   flit publish

check:
    pdm run mypy --allow-redefinition --strict plaid2/

test:
    pdm run pytest

lint:
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=__pypackages__,.venv
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --ignore=F401,E501,F841 --exclude=__pypackages__,.venv


run *ARGS:
    pdm run python {{ARGS}}
