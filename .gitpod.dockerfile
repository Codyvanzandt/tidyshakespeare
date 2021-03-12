FROM gitpod/workspace-full

RUN echo 'alias run_tests="cd $GITPOD_REPO_ROOT && python -m pytest -s -v"' >> $HOME/.bashrc
