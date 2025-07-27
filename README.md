## MCTS
A simple MCTS implementation in python.

The implementation is general enough that it can easily be integrated with any game for which MCTS is applicable. The rollout policy samples randomly from available moves. This does make the simulations slower because of the added noise but it gives freedom to the user to implement their own rollout policy specific to the domain of application.

An example is also supplied for tictactoe for demonstration.

## Usage
### Install Requirements
```sh
pip install -r requirements.txt
```

### And Go!
```sh
python main.py
```

## Learn More
[Numberphile Video](https://www.youtube.com/watch?v=BEFY7IHs0HM)

[A Survey of Monte Carlo Tree Search Methods](https://ieeexplore.ieee.org/document/6145622)
