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
    mypy --allow-redefinition --strict plaid2/

test:
    pytest --ignore=__pypackages__
