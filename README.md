# Dynamic Publisher Subscriber Mark Framework (DPSMF)

The DPSMF searches a project for `yaml` files with a certain naming convention and generates
boilerplate APIs for each of the files found. The boilerplate text, as the project name implies, is
for publishers, subscribers, and mock code.

- Publishers: Code that creates data and wants to share it
- Subscribers: Code that wants to get data from a publisher
- Mock: Code that imitates the behavior of a real system

Along with the boilerplate code, a document outlining the API created will also be generated at the
location specified by the `out_dir` option. There are two main targets for this project:

- [Simulation](https://github.com/alexb7711/GMSE)
- Actual implementation framework (TBD)

# TODO: Quick Start

To initialize the program, the `base_path` must be specified from where you wish the program to
begin recursively searching for appropriately named YAML files. The naming convention for the YAML
file goes as follows: `[type]_[name].yml`. As an example, if one wishes to create a `publisher`
called `position`, the required file name would be `pub_position.yml`.

TODO: General formatting

The following section contain explanations for the parameters of each of the allowed types.

## TODO Variable/Parameter Specification

- [ ] Variable/Parameter API
    - [ ] Int
    - [ ] Float
    - [ ] String
    - [ ] Boolean
    - [ ] Arrays

## TODO Publisher/Subscriber/Mock Specification

- [ ] Type API
- [ ] Publisher API
- [ ] Subscriber API
- [ ] Mock API

## Simulation

The simulation aspect will generate the publishers, subscribers, _and_ mock frameworks. By default
DPSMF will generate just the publishers and subscribers, meaning that the mock interfaces will be
generated only if the `enable_mock` option is set to `true`.

## TODO: Implementation

# Supported Languages
- [ ] Python
- [ ] Rust
- [ ] C/C++

