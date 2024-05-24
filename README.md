# Dynamic Publisher Subscriber Mark Framework (DPSMF)
The DPSMF searches a project for `yaml` files with a certain naming convention and generates boilerplate APIs for each of the files found. The boilerplate text, as the project name implies, is for publishers, subscribers, and mock code.

- Publishers: Code that creates data and wants to share it
- Subscribers: Code that wants to get data from a publisher
- Mock: Code that imitates the behavior of a real system

Along with the boilerplate code, a document outlining the API created will also be generated at the location specified by the `out_dir` option. There are two main targets for this project:

- [Simulation](https://github.com/alexb7711/GMSE)
- Actual implementation framework (TBD)

# TODO: Quick Start

## Variable/Parameter Specification
- [ ] Variable/Parameter API
    - [ ] Int
    - [ ] Float
    - [ ] String
    - [ ] Boolean
    - [ ] Arrays

## Publisher/Subscriber/Mock Specification
- [ ] Type API
    - [ ] Publisher API
    - [ ] Subscriber API
    - [ ] Mock API

## Simulation
The simulation aspect will generate the publishers, subscribers, _and_ mock frameworks. By default DPSMF will generate just the publishers and subscribers, meaning that the mock interfaces will be generated only if the `enable_mock` option is set to `true`. 

## TODO: Implementation 

# Supported Languages
- [ ] Python
- [ ] Rust
- [ ] C/C++

