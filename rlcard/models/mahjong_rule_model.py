''' MAHJONG rule models
'''

import numpy as np

import rlcard
from rlcard.models.model import Model

class MAHJONGRuleAgentV1(object):
    ''' MAHJONG Rule agent version 1
    '''

    def __init__(self):
        pass

    def step(self, state):
        ''' Predict the action given raw state. A naive rule. We set a naive rule,
            by which the next card is played by judging the type and combination of the cards in the hand.
            The goal is to increase the number of equal or consecutive cards in the hand as much as possible.
            To achieve this, we score every card in hand and play the card with the minimum value.

        Args:
            state (dict): Raw state from the game
        Returns:
            action (str): Predicted action
        '''

        legal_actions = state['legal_actions']
        if 'play' in legal_actions:
            return 'play'

        hand = state['hand']


        for action in legal_actions:
            if action == 'play':


                hand = [card.get_str() for card in player.hand]
                i = []
                scores = [0]*14
                b = 0
                for card in hand:
                    card = card.split('-')
                    i = i.append[card]
                for c in i:
                    for c2 in i:
                        if c == c2:
                            scores[b] += 100
                        elif c[0] == c2[0] and abs(int(c[1])-int(c2[1])) < 2:
                            scores[b] += 20
                        elif c[0] == c2[0] and abs(int(c[1])-int(c2[1])) < 3:
                            scores[b] += 10
                        b += 1
                pc = scores.index(min())
                action = 'play'

                card = player.hand[pc]
                dealer.table.append(card)

                reture action



        # Otherwise, we randomly choose one
        action = np.random.choice(self.filter_wild(legal_actions))
        return action




class MahjongRuleModelV1(Model):
    ''' Mahjong Rule Model version 1
    '''

    def __init__(self):
        ''' Load pretrained model
        '''
        env = rlcard.make('mahjong')

        rule_agent = MAHJONGRuleAgentV1()
        self.rule_agents = [rule_agent for _ in range(env.player_num)]

    @property
    def agents(self):
        ''' Get a list of agents for each position in a the game
        Returns:
            agents (list): A list of agents
        Note: Each agent should be just like RL agent with step and eval_step
              functioning well.
        '''
        return self.rule_agents

    @property
    def use_raw(self):
        ''' Indicate whether use raw state and action
        Returns:
            use_raw (boolean): True if using raw state and action
        '''
        return True