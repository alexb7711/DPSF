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

[Full documentation can be found here](https://alexb7711.github.io/DPSMF/index.html)

TODO: General formatting

The following section contain explanations for the parameters of each of the allowed types.

## TODO Supported Variables and Specification

- [ ] Variable/Parameter API
    - [ ] Int
    - [ ] Float
    - [ ] String
    - [ ] Boolean
    - [ ] Arrays

## TODO Publisher/Subscriber/System API Specification
Publishers, subscribers, and system YAML files define the parameters required to generated instances
for each of their respective types. At a high level, publishers provide data to the system,
subscribers listen to the published data, and system files are general purpose glue code to
interface with hardware drivers and simulation.

### Publishers
The figure below describes how publishers interact with DPSMF. When a publisher is created, the
parameters specified by the publisher are used too

1) generate subscriber code in the directory the YAML file was found and
2) create an internal representation of the data structure in DPSMF.

The file generated provide the necessary code to be able to publish whatever information its
provided to the DPSMF client. Once the data has been published to the client (whether it be a local
or remote client), it is the job of the DPSMF client too

1) store the data in a database and
2) transmit the data utilizing the specified mode of transmission (TCP, UDP, RF, etc.)

The database can be transient in the sense that it only keeps the latest information (i.e., used to
reduce storage footprint), or it can be persistent to store specific or all data provided for
logging and playback purposes.


![Publisher UML Diagram](./img/types/publisher.png "Publisher Component Diagram")

### TODO: Subscribers
### TODO: Systems

- [ ] Type API
    - [ ] Publisher API
    - [ ] Subscriber API
    - [ ] System API

## Simulation

The simulation aspect will generate the publishers, subscribers, _and_ mock frameworks. By default
DPSMF will generate just the publishers and subscribers, meaning that the mock interfaces will be
generated only if the `enable_mock` option is set to `true`.

## TODO: Implementation

# Supported Languages
- [ ] Python
- [ ] Rust
- [ ] C/C++

