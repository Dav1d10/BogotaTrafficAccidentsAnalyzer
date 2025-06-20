# BogotaTrafficAccidentsAnalyzer
<!-- PROJECT SHIELDS -->
[![License][challenge3-license-shield]][challenge3-license-url]

## Description

This Python application project was developed as part of the **ISIS1225 Estructuras de Datos y Algoritmos (DSA)** course at _Universidad de Los Andes_. It allows users to analyze traffic accident data in Bogotá by loading CSV files and executing various queries through a command-line interface.

The system is structured following the **Model-View-Controller (MVC)** pattern and leverages advanced data structures such as **Binary Search Trees (BST)** and **Red-Black Trees (RBT)**, along with linear structures like lists, stacks, queues, and hash tables, to ensure efficient storage and retrieval of information.

The dataset includes detailed records of traffic accidents in Bogotá from 2015 to 2022, enabling functionalities such as filtering by date ranges, severity, accident type, geographic location, and time of day.

## Repository Information

This repository is part of the Data Structures and Algorithms (#EDA) teaching framework at Universidad de los Andes. The repository was developed by faculty professors and staff in the Department of Systems and Computer Engineer (#DISC) and uses the Non-Object-Oriented Python library **DISCLib**.

[DISClib][disclib-url] · [DISClib Demo and Examples][demo-url] · [Report Bug][challenge3-bugs-url] · [Request Feature][challenge3-issues-url]

## Project Documentation

- [Project Context and Requirements](Docs/ProjectOverview.pdf)
- [Project Analysis](Docs/ProjectAnalysis.pdf)

## Members

- David Caro
- Alejandro Abril
- Gabriel Martinez

[Back to top](#bogotatrafficaccidentsanalyzer)

<!-- ABOUT THE PROJECT -->
## About The Project

This is a template repository to use in the project implementation for the data structures and algorithms (#EDA) course at Uniandes.

**IMPORTANT** This is a work in progress and is part of a teaching framework for undergraduate college students at Universidad de los Andes. This project Is NOT intended as a full-functional source code project.

[Back to top](#bogotatrafficaccidentsanalyzer)

## Repository Structure

The project is organized into four main folders:

- `BogotaTrafficAccidentsAnalyzer/`
    - `App`: [App](./App) Folder with the model-view-controller (MVC) Python scripts.
    - `DISClib`: [DISClib](./DISClib) Root folder with the official course library. For more on its implementation visit the [DISClib Repository][disclib-url].
    - `Data`: [Data](./Data) Folder with CSV data files to load into the application.
    - `Docs`: [Docs](./Docs) Folder with the reports, data table and other documentation.

[Back to top](#bogotatrafficaccidentsanalyzere)

## Prerequisites

To run this project locally, make sure you have the following installed:

- **Python 3.8 or higher** – Required to run the application.
  Check your version with
```bash
  python --version
  ```
- **pip** – Python package installer (usually included with Python).
  Check with
```bash
  pip --version
  ```
- **tabulate** – For printing formatted tables in the terminal.
```bash
  pip install tabulate
  ```
- **matplotlib** – Required for generating visualizations like histograms.
```bash
  pip install matplotlib
  ```

## How to run

Follow these steps to run the application locally:

1. Clone the repository
```bash
  git clone https://github.com/Dav1d10/BogotaTrafficAccidentsAnalyzer.git
  ```
2. Open a terminal and navigate to the `App` folder
```bash
  cd App
  ```
3. Execute the main script `view.py` from the terminal
```bash
  python view.py
  ```

<!-- USAGE EXAMPLES -->
## Usage

To use this template, you need to follow the steps below:

* Read the official project document published in the course official site at [BrightSpace][BrightSpace-url].
* Distribute the project functionalities and implementation responsibilities between to the group members.
* Download the official dataset for the project at the course official site at[BrightSpace][BrightSpace-url].
* Unzip and load the dataset into the application at [Data](./Data) folder.
* Import the necessary modules from [DISClib](./DISClib) into the MVC scripts at [App](./App) folder.
* Implement the missing functions according to the project needs in the MVC scripts at [App](./App) folder.
* Evaluate the implementation of the MVC scripts, record your tests and analysis in the documents at [Docs](./Docs) folder (The report **MUST BE** in PDF format).

[Back to top](#bogotatrafficaccidentsanalyzer)

<!-- CONTACT -->
## Contact and support

For further information and contact, use the following links:

* Official Repository [DISClib][disclib-url].
* Repository for [Demo and Examples][demo-url].
  
If you require further information, please contact us [via this email](mailto:isis1225@uniandes.edu.co)

[Back to top](#bogotatrafficaccidentsanalyzer)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

[Back to top](#bogotatrafficaccidentsanalyzer)

<!-- LICENSE -->
## License

Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes.
Developed for the class _"ISIS1225 - Estructuras de Datos y Algoritmos"_ or _"ISIS1225 - Data Structure and Algorithms"_ in english.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU General Public License](LICENSE) for more information go to [GNU ORG][gnu-url].

[Back to top](#bogotatrafficaccidentsanalyzer)

<!-- ACKNOWLEDGMENTS -->
## Authors and acknowledgment

* [Dario Correal][dariocorreal-url] is the original author and main developer of the library.
* [Santiago Arteaga][phillipus85-url] is a contributor and repository administrator. 
* [Luis Florez][le99-url] is a contributor and developed examples and tutorials for the library.

[Back to top](#bogotatrafficaccidentsanalyzer)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- links for DISClib -->
[contributors-shield]: https://img.shields.io/github/contributors/ISIS1225DEVS/ISIS1225-Lib.svg?style=for-the-badge
[contributors-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ISIS1225DEVS/ISIS1225-Lib.svg?style=for-the-badge
[forks-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/network/members
[stars-shield]: https://img.shields.io/github/stars/ISIS1225DEVS/ISIS1225-Lib.svg?style=for-the-badge
[stars-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/stargazers
[issues-shield]: https://img.shields.io/github/issues/ISIS1225DEVS/ISIS1225-Lib.svg?style=for-the-badge
[issues-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/issues
[license-shield]: https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge
[license-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/blob/master/LICENSE
<!-- [linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png -->
[uniandes-url]: https://cursos.virtual.uniandes.edu.co/isis1225/
[BrightSpace-url]: https://bloqueneon.uniandes.edu.co/d2l/home
[organization-url]: https://github.com/ISIS1225DEVS/
[disclib-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib
[demo-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples
[bugs-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/issues
[issues-url]: https://github.com/ISIS1225DEVS/ISIS1225-Lib/issues
[gnu-url]: http://www.gnu.org/licenses/
<!-- contributors  -->
[dariocorreal-url]: https://github.com/dariocorreal
[phillipus85-url]: https://github.com/phillipus85
[le99-url]: https://github.com/le99
<!-- EDA lab + challenges repository -->
[sample-mvc-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleMVC
[sample-conflicts-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleConflicts
[sample-list-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleList
[sample-sort-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleSorts
[sample-map-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleMap
[sample-collision-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleCollision
[sample-tree-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleTree
[sample-graph-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleGraph
[sample-algorithm-url]: https://github.com/ISIS1225DEVS/ISIS1225-SampleAlgorithm
[challenge1-url]: https://github.com/ISIS1225DEVS/Reto1-Template
[challenge2-url]: https://github.com/ISIS1225DEVS/Reto2-Template
[challenge3-url]: https://github.com/ISIS1225DEVS/Reto3-Template
[challenge4-url]: https://github.com/ISIS1225DEVS/Reto4-Template

<!-- links for EDA examples repository -->
[demo-contributors-shield]: https://img.shields.io/github/contributors/ISIS1225DEVS/ISIS1225-Examples.svg?style=for-the-badge
[demo-contributors-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples/graphs/contributors
[demo-forks-shield]: https://img.shields.io/github/forks/ISIS1225DEVS/ISIS1225-Examples.svg?style=for-the-badge
[demo-forks-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples/network/members
[demo-stars-shield]: https://img.shields.io/github/stars/ISIS1225DEVS/ISIS1225-Examples.svg?style=for-the-badge
[demo-stars-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples/stargazers
[demo-issues-shield]: https://img.shields.io/github/issues/ISIS1225DEVS/ISIS1225-Examples.svg?style=for-the-badge
[demo-issues-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples/issues
[demo-license-shield]: https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge
[demo-license-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples/blob/master/LICENSE
[demo-bugs-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples/issues
[demo-issues-url]: https://github.com/ISIS1225DEVS/ISIS1225-Examples/issues

<!-- links for EDA Sample-Reto3 challenge repository -->
[challenge3-contributors-shield]: https://img.shields.io/github/contributors/ISIS1225DEVS/Reto3-Template.svg?style=for-the-badge
[challenge3-contributors-url]: https://github.com/ISIS1225DEVS/Reto3-Template/graphs/contributors
[challenge3-forks-shield]: https://img.shields.io/github/forks/ISIS1225DEVS/Reto3-Template.svg?style=for-the-badge
[challenge3-forks-url]: https://github.com/ISIS1225DEVS/Reto3-Template/network/members
[challenge3-stars-shield]: https://img.shields.io/github/stars/ISIS1225DEVS/Reto3-Template.svg?style=for-the-badge
[challenge3-stars-url]: https://github.com/ISIS1225DEVS/Reto3-Template/stargazers
[challenge3-issues-shield]: https://img.shields.io/github/issues/ISIS1225DEVS/Reto3-Template.svg?style=for-the-badge
[challenge3-issues-url]: https://github.com/ISIS1225DEVS/Reto3-Template/issues
[challenge3-license-shield]: https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge
[challenge3-license-url]: https://github.com/ISIS1225DEVS/Reto3-Template/blob/master/LICENSE
[challenge3-bugs-url]: https://github.com/ISIS1225DEVS/Reto3-Template/issues
[challenge3-issues-url]: https://github.com/ISIS1225DEVS/Reto3-Template/issues
