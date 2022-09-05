# pyCosmicWrap 🌯
_A python3 wrapper around Cosmos API/RPC brought to you by [ChihuahuaChain](https://chihuahua.wtf)_

# Info
pyCosmicWrap 🌯 makes it easier to develop python applications on the Cosmos Ecosystem.
It currently has been tested with ChihuahuaChain and the first stable release will have it production-ready for almost every Cosmos Blockchain

# Todo
There's a lot more to add, here's our plan, feel free to contribute with code improvements, testing and feel free to push a PR to help us to improve pyCosmicWrap and to make it the default choice for any Cosmos Ecosystem python developer. The next big step will be adding [Mospy by ctrl-Felix](https://github.com/ctrl-Felix/mospy) in order to be able to create and broadcast transactions as well.

- [x] Wrap main default API endpoints
- [ ] Wrap main RPC endpoints
- [ ] Add Osmosis specific endpoints
- [ ] Publish on PyPi
- [ ] Integrate [Mospy by ctrl-Felix](https://github.com/ctrl-Felix/mospy)

## Installation

You can install this module with
`python -m pip install pyCosmicWrap`


## Bank Queries
- `query_balances(address)` _queries the balance of all coins for a single account_
- `query_balances_by_udenom(address, udenom)` _queries the balance of a single coin for a single account._
- `query_supply()` _queries the total supply of all coins._
- `query_supply_by_udenom(udenom)` _queries the supply of a single coin._

## Distribution Queries
- `query_community_pool()` _queries the community pool coins_
- `query_distribution_params()` _queries the blockchain distribution parameters_
- `query_rewards(delegator)` _queries the total rewards accrued by a each validator_
- `query_rewards_by_validator(delegator, validator)` _queries the total rewards accrued by a delegation on a given validator_
- `query_delegator_validators(delegator)` _queries the validators of a delegator_
- `query_withdraw_address(delegator)` _queries withdraw address of a delegator_
- `query_commission(validator)` _queries accumulated commission for a validator_
- `query_outstanding_rewards(validator)` _queries rewards of a validator address_

## Governance Queries
- `query_proposals()` _queries all the proposals_
- `query_proposal_by_id(id)` _queries a specific proposal by a given id (accepts both string or integers)_
- `query_tally(id)` _queries tally of a proposal by a given id (accepts both string or integers)_
- `query_votes(id)` _queries votes for a specific proposal by a given id (accepts both string or integers)_
- `query_votes_by_address(id, address)` _queries votes for a specific proposal from a given address (accepts both string or integers)_

## Slashing Queries
- `query_slashing_params()` _queries slashing parameters_

## Staking Queries
- `query_staking_params()` _queries staking parameters_
- `query_staking_pool()` _queries staking pool_
- `query_delegations_by_address(delegator)` _queries all the delegations of a given address_
- `query_redelegations_by_address(delegator)` _queries all the redelegations of a given address_
- `query_unbonding_by_address(delegator)` _queries all the unbondings of a given address_
- `query_delegator_data(delegator)` _queries delegator data of a given address_
- `query_delegator_data_by_validator(delegator, validator)` _queries delegator data of a given address on a given validator_
- `query_all_validators()` _queries all the validators_
- `query_validator_by_address(validator)` _queries data for a given validator_
- `query_delegators(validator)` _queries all the delegators for a given validator_
- `query_delegators_by_address(validator, delegator)` _queries a given delegator's data for a given validator_
- `query_validator_unbonding_by_address)` _queries a given delegator's unbonding data for a given validator_
- `query_unbonding_from(validator)` _queries all the unbonding of a give validator_

# Examples

#### Initialize the module and print basic info
```python
from pyCosmicWrap import CosmicWrap

# create an object with rest api url, rpc url and udenom as arguments
chihuahua = CosmicWrap(lcd='https://api.chihuahua.wtf',
                       rpc='https://rpc.chihuahua.wtf',
                       udenom='uhuahua')

# Once the module is imported and the object is created we can start using
# the object to interact with the blockchain

# Let's define an address
my_address = 'chihuahua1z6rfp8wzsx87pwt3z73gf2a67d6tgmfrrlzy7p'

# Let's create a variable with your balance
my_address_balance = chihuahua.query_balance(my_address)

# or just print it out
print(my_address_balance)

# check all of your delegations
my_delegations = chihuahua.query_delegations_by_address(my_address)

# and print them out
print(my_delegations)

# check all of your staking rewards
print(chihuahua.query_rewards(my_address))

```


# Donate
We don't seek for donations, but you can say Thank You for our work by [delegating to our validators](https://delegate.chihuahua.wtf) and by [sharing this project on Twitter](https://twitter.com/intent/tweet?text=Check%20out%20%23pyCosmicWrap%20%F0%9F%8C%AF%20by%20%40ChihuahuaChain%20-%20A%20%23python%20wrapper%20for%20%40cosmos%20on%20https%3A//github.com/ChihuahuaChain/pyCosmicWrap%20%23HUAHUA%20%23Chihuahua%20%23WOOF%0A)

# License
ChihuahuaChain/pyCosmicWrap is licensed under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
