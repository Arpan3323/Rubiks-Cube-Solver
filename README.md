# Rubik's Cube Solver

## About
A Flask microservice that solves a rubik's cube by returning the rotations required to solve an input rubik's cube. Developed using [Test-Driven-Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development).

## Usage
### Accessing through URL
 The application has been deployed in a containerized environment with Docker and Azure Web App Service. You can access the application homepage at the following URL: https://rubikscubesolver.azurewebsites.net/ 

**Note:** The application is deployed on a free tier, so it may take a few seconds to load.

To get the rotations required to solve a rubik's cube, you can simply pass your Rubik's cube as a query parameter to the URL below. Make sure to replace `<cube>` with your Rubik's cube's color configuration:
```
https://rubikscubesolver.azurewebsites.net/rubik/solve?cube=<cube>
```
#### Example:
- Input: `https://rubikscubesolver.azurewebsites.net/rubik/solve?cube=grgggggggobooooooobobbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww`

    - The `<cube>` parameter here has been replaced with the string `"grgggggggobooooooobobbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww"`. This represents the color configuration of the Rubik's cube. The order of the characters represents the order of the colors on each face of your Rubik's cube, starting from the front face and going to the right, back, left, top, and bottom faces. For each face, start by noting the color at the top left corner and end by noting the color at the bottom right corner. The colors are represented as follows:

        - `g`: green
        - `r`: red
        - `b`: blue
        - `o`: orange
        - `y`: yellow
        - `w`: white 

- Output: `{'solution': 'FFUrLFFlRUFFRRUbFRRfBURR', 'status': 'ok', 'integrity': 'd9d04fc8'}`

    - The rotations required to solve the Rubik's cube are `FFUrLFFlRUFFRRUbFRRfBURR`. Each character represents a rotation of a face of the Rubik's cube. The characters are represented as follows:

        - `F`: rotate the front face clockwise
        - `R`: rotate the right face clockwise
        - `B`: rotate the back face clockwise
        - `L`: rotate the left face clockwise
        - `U`: rotate the top face clockwise
        - `f`: rotate the front face counter-clockwise
        - `r`: rotate the right face counter-clockwise
        - `b`: rotate the back face counter-clockwise
        - `l`: rotate the left face counter-clockwise
        - `u`: rotate the top face counter-clockwise

    - The `integrity` field is a substring of the SHA256 hash of the input Rubik's cube. You can use this field to verify that the returned solution is for the Rubik's cube you passed in.

You can also use tools like [Postman](https://www.postman.com/) or [cURL](https://en.wikipedia.org/wiki/CURL) to make GET requests to the URL above.

#### Example using cURL:
```CLI
curl https://rubikscubesolver.azurewebsites.net/rubik/solve?cube=grgggggggobooooooobobbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww
```


## Development Process

- **Analysis Phase**: Conducted analysis, including writing acceptance tests.
- **Pre-Architecture Phase**: Utilized CRC cards to describe classes, methods, and their interdependencies.
- **Planning Phase**: Estimated expected time and lines of code for the current iteration.
- **Construction Phase**: Followed Test Driven Development (TDD) approach, writing tests first and implementing code to pass them. Iteratively implemented planned architecture using CRC cards.
- **Review Phase**: Reviewed test code, ensuring comprehensive coverage of boundary values for each iteration. Used rubber duck debugging methodology.
- **Refactor Phase**: Refactored production code to remove code smells. If new boundary values were identified during the review phase, then go back to construction.
- **Post-Architecture Phase**: Revisited CRC cards, defining the actual implemented architecture for the current iteration. Compared Pre-Architecture and Post-Architecture CRC cards, identifying differences and questioning reasons for deviations.
- **Postmortem Phase**: Recorded actual lines of code and time for each phase in the current iteration. Analyzed differences between actual and expected time, questioning factors leading to over-estimation or under-estimation of total time recorded during planning phase.

## Upcoming Features
- A React frontend that allows users to input their Rubik's cube and get the rotations required to solve it. The frontend will also display a 3D model of the Rubik's cube that users can interact with.

## Contributions
Contributions are welcome! Please feel free to open an issue or submit a pull request. 
