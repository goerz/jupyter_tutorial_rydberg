# Jupyter/QuTiP Tutorial: Rydberg atoms

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/goerz/jupyter_tutorial_rydberg/master)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/goerz/jupyter_tutorial_rydberg)
[![Youtube](https://img.shields.io/badge/Youtube%20Videos-2-red)](https://www.youtube.com/playlist?list=PLD3uZJ5Hp3yvUGxs0xAArlAmzPIdDZpcg)

This repository contains notebooks for a tutorial giving an introduction to using Jupyter Notebooks and using [QuTiP][] and the [krotov][] package to simulate and optimize the dynamics of a system of Rydberg atoms.

A recording of the tutorial is available on [YouTube](https://www.youtube.com/playlist?list=PLD3uZJ5Hp3yvUGxs0xAArlAmzPIdDZpcg):

* [Part 1](https://www.youtube.com/watch?v=PKjXgvGUSp4&list=PLD3uZJ5Hp3yvUGxs0xAArlAmzPIdDZpcg&index=2&t=0s): installing Miniconda, creating an `environment.yml`, creating a conda environment, Git, Github, installing Github Desktop, creating a git repository, running the Jupyter notebook interface
* [Part 2](https://www.youtube.com/watch?v=JqKOw-EBCLo&list=PLD3uZJ5Hp3yvUGxs0xAArlAmzPIdDZpcg&index=2&t=0s): Jupyter notebook basics, making git commits (snapshots) and pushing to Github, Cloning git repositories from Github, using `qutip`, using `matplotlib`, using `krotov`.

**Questions/Problems?**

[Open an Issue!](https://github.com/goerz/jupyter_tutorial_rydberg/issues/new/choose)


## Instructions

* Install [miniconda][] [[Part 1, 0:01:10](https://youtu.be/PKjXgvGUSp4?t=70)]. If you have the more complete [Anaconda][], that's ok, too.

* Install [Github Desktop][] [[Part 1, 1:00:47](https://youtu.be/PKjXgvGUSp4?t=3647)]

* Clone the repository to your computer, [using Github Desktop][clone-gh-desktop] [[Part 2, 0:24:42](https://youtu.be/JqKOw-EBCLo?t=1482)]

* Open a shell, and navigate to the "project folder" (the cloned repository)  [[Part 2, 0:25:22](https://youtu.be/JqKOw-EBCLo?t=1522)]

* Create the [conda virtual environment][] for the project [[Part 2, 0:25:48](https://youtu.be/JqKOw-EBCLo?t=1548)]:

      conda env create -p .venv -f environment.yml

  You only need to do this once per "checkout" of the repository. If you need additional packages, edit `environment.yml`, delete the `.venv` folder, and re-create the environment.

* Activate the project environment (`conda activate .\.venv` on Windows [[Part 1, 1:25:42](https://youtu.be/PKjXgvGUSp4?t=5142)], `conda activate ./.venv` on macOS/Linux [[Part 2, 0:29:00](https://youtu.be/JqKOw-EBCLo?t=1740) (Mac)]. Note that `conda activate .venv` does not work!

* Run the jupyter notebook server [[Part 1, 1:27:28](https://youtu.be/PKjXgvGUSp4?t=5248) (Windows), [Part 2, 0:29:27](https://youtu.be/JqKOw-EBCLo?t=1767) (Mac)]:

      jupyter notebook --debug

  This should open the Jupyter notebook interface in your browser.

* Activate the [Jupyter Notebook Extensions][]. You'll want [Execute Time][] and [Table of Contents (2)][] [[Part 1, 1:30:28](https://youtu.be/PKjXgvGUSp4?t=5428)]. You only need to do this once.

* Open the notebooks and run them [[Part 2, 0:30:10](https://youtu.be/JqKOw-EBCLo?t=1810)]


## Reading list

* [Pro Git Book][1]
* [Conda Documentation][2]
* [Jupyter documentation][3]
* [Python tutorial][4]
* [Scipy.org][5]. This links to the documentation for the most important packages in the scientific Python ecosystem (NumPy, SciPy, IPython, SymPy, pandas)
* [QuTiP documentation][6]. Package for the numerical description of quantum systems, with solvers for the Schrödinger and Liouville-von-Neumann equations
* [krotov documentation][7]. Optimization package on top of QuTiP

[QuTiP]: http://qutip.org
[krotov]: https://github.com/qucontrol/krotov
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Anaconda]: https://www.anaconda.com/products/individual
[Github Desktop]: https://desktop.github.com
[clone-gh-desktop]: https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-a-repository-from-github-to-github-desktop
[conda virtual environment]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
[Jupyter Notebook Extensions]: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/
[Execute Time]: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/execute_time/readme.html
[Table of Contents (2)]: https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/toc2/README.html
[1]: https://git-scm.com/book/en/v2
[2]: https://docs.conda.io/projects/conda/
[3]: https://jupyter.readthedocs.io/
[4]: https://docs.python.org/3/tutorial/
[5]: https://www.scipy.org
[6]: http://qutip.org/docs/latest/index.html
[7]: https://qucontrol.github.io/krotov/v1.2.0/
