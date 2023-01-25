# pyCosmicWrap is a Cosmos API/RPC python Wrapper
# ChihuahuaChain - https://github.com/ChihuahuaChain/pyCosmicWrap
#
# License GNU General Public License v3.0
#
# https://choosealicense.com/licenses/gpl-3.0/
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
from urllib.parse import quote

import requests


class CosmicWrap:
    def __init__(self, lcd: str, rpc: str, denom: str):
        self.lcd = lcd
        self.rpc = rpc
        self.denom = denom

    # queries the balance of all coins for a single account.
    def query_balances(self, address: str):
        responses = []
        endpoint = '/cosmos/bank/v1beta1/balances/'
        try:
            results = json.loads(requests.get(self.lcd + endpoint + address, timeout=60).content)
            responses += results['balances']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + '?pagination.key=' + quote(str(pagination)), timeout=60).content)
                responses += results['balances']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries the balance of a given denom for a single account.
    def query_balances_by_denom(self, address, denom):
        endpoint = '/cosmos/bank/v1beta1/balances/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/by_denom?denom=' + denom, timeout=60).content)
        except Exception:
            raise Exception

    # queries the total supply of all coins.
    def query_supply(self):
        endpoint = '/cosmos/bank/v1beta1/supply'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries the total supply of a given denom.
    def query_supply_by_denom(self, denom):
        denom = self.denom if denom is None else denom
        endpoint = '/cosmos/bank/v1beta1/supply/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + denom, timeout=60).content)
        except Exception:
            raise Exception

    # queries the community pool coins.
    def query_community_pool(self):
        endpoint = '/cosmos/distribution/v1beta1/community_pool'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries the total rewards accrued by every validator.
    def query_rewards(self, address):
        endpoint = '/cosmos/distribution/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/rewards', timeout=60).content)
        except Exception:
            raise Exception

    # queries the total rewards accrued by a given validator.
    def query_rewards_by_validator(self, address, validator):
        endpoint = '/cosmos/distribution/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/rewards/' + validator, timeout=60).content)
        except Exception:
            raise Exception

    # queries the validators of a delegator.
    def query_delegator_validators(self, address):
        endpoint = '/cosmos/distribution/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/validators', timeout=60).content)
        except Exception:
            raise Exception

    # queries withdraw address of a delegator.
    def query_withdraw_address(self, address):
        endpoint = '/cosmos/distribution/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/withdraw_address', timeout=60).content)
        except Exception:
            raise Exception

    # queries params of the distribution module.
    def query_distribution_params(self):
        endpoint = '/cosmos/distribution/v1beta1/params'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries accumulated commission for a validator.
    def query_commission(self, validator):
        endpoint = '/cosmos/distribution/v1beta1/validators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + validator + '/commission', timeout=60).content)
        except Exception:
            raise Exception

    # queries accumulated rewards for a validator.
    def query_outstanding_rewards(self, address):
        endpoint = '/cosmos/distribution/v1beta1/validators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/outstanding_rewards', timeout=60).content)
        except Exception:
            raise Exception

    # queries all proposals
    def query_proposals(self, status=None):
        responses = []
        endpoint = '/cosmos/gov/v1beta1/proposals'
        if status == 'PROPOSAL_STATUS_UNSPECIFIED':
            endpoint += '?proposalStatus=0'
        elif status == 'PROPOSAL_STATUS_DEPOSIT_PERIOD':
            endpoint += '?proposalStatus=1'
        elif status == 'PROPOSAL_STATUS_VOTING_PERIOD':
            endpoint += '?proposalStatus=2'
        elif status == 'PROPOSAL_STATUS_PASSED':
            endpoint += '?proposalStatus=3'
        elif status == 'PROPOSAL_STATUS_REJECTED':
            endpoint += '?proposalStatus=4'
        elif status == 'PROPOSAL_STATUS_FAILED':
            endpoint += '?proposalStatus=5'
        try:
            results = json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
            responses += results['proposals']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + '?pagination.key=' + quote(str(pagination)), timeout=60).content)
                responses += results['proposals']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries a proposal by a given id
    def query_proposals_by_id(self, proposal_id):
        endpoint = '/cosmos/gov/v1beta1/proposals/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + str(proposal_id), timeout=60).content)
        except Exception:
            raise Exception

    # queries the tally of a proposal by a given id
    def query_tally(self, proposal_id):
        endpoint = '/cosmos/gov/v1beta1/proposals/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + str(proposal_id) + '/tally', timeout=60).content)
        except Exception:
            raise Exception

    # queries the votes of a proposal by a given id
    def query_votes(self, proposal_id):
        responses = []
        endpoint = '/cosmos/gov/v1beta1/proposals/'
        try:
            results = json.loads(requests.get(self.lcd + endpoint + str(proposal_id) + '/votes', timeout=60).content)
            responses += results['votes']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + str(proposal_id) + '/votes' + '?pagination.key=' + quote(
                        str(pagination)), timeout=60).content)
                responses += results['votes']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries a voter of a given proposal.
    def query_votes_by_address(self, proposal_id, address):
        endpoint = '/cosmos/gov/v1beta1/proposals/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + str(proposal_id) + '/votes/' + address, timeout=60).content)
        except Exception:
            raise Exception

    # queries the slashing parameters
    def query_slashing_params(self):
        endpoint = '/cosmos/slashing/v1beta1/params'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries delegations of a given address
    def query_delegations_by_address(self, address):
        endpoint = '/cosmos/staking/v1beta1/delegations/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + address, timeout=60).content)
            responses += results['delegation_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + address + '?pagination.key=' + quote(str(pagination)), timeout=60).content)
                responses += results['delegation_responses']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries redelegations by a given address
    def query_redelegation_by_address(self, address):
        endpoint = '/cosmos/staking/v1beta1/delegators/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + address + '/redelegations', timeout=60).content)
            responses += results['redelegation_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + address + '/redelegations?pagination.key=' + quote(str(pagination)), timeout=60).content)
                responses += results['delegation_responses']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries unbondings by a given address
    def query_unbonding_by_address(self, address):
        endpoint = '/cosmos/staking/v1beta1/delegators/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + address + '/unbonding_delegations', timeout=60).content)
            responses += results['unbonding_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + address + '/unbonding_delegations?pagination.key=' + quote(
                        str(pagination)), timeout=60).content)
                responses += results['unbonding_responses']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries delegator data
    def query_delegator_data(self, address):
        endpoint = '/cosmos/staking/v1beta1/delegators/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + address + '/validators', timeout=60).content)
            responses += results['validators']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + address + '/validators?pagination.key=' + quote(str(pagination)), timeout=60).content)
                responses += results['validators']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries delegator data of a given address on a given validator
    def query_delegator_data_by_validator(self, address, validator):
        endpoint = '/cosmos/staking/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/validators/' + validator, timeout=60).content)
        except Exception:
            raise Exception

    # queries staking parameters
    def query_staking_params(self):
        endpoint = '/cosmos/staking/v1beta1/params'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries staking pool
    def query_staking_pool(self):
        endpoint = '/cosmos/staking/v1beta1/pool'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries all the validators
    def query_all_validators(self):
        endpoint = '/cosmos/staking/v1beta1/validators'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
            responses += results['validators']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + '?pagination.key=' + quote(str(pagination)), timeout=60).content)
                responses += results['validators']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries a validator by a given address
    def query_validator_by_address(self, address):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address, timeout=60).content)
        except Exception:
            raise Exception

    # queries delegators of a given validator
    def query_delegators(self, validator):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + validator + '/delegations', timeout=60).content)
            responses += results['delegation_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + validator + '/delegations?pagination.key=' + quote(str(pagination)), timeout=60).content)
                responses += results['delegation_responses']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries a validator for a specific delegator address
    def query_delegators_by_address(self, validator, address):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + validator + '/delegations/' + address, timeout=60).content)
        except Exception:
            raise Exception

    # queries a validator for a specific unbonding address
    def query_validator_unbonding_by_address(self, validator, address):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        try:
            return json.loads(requests.get(
                self.lcd + endpoint + validator + '/delegations/' + address + '/unbonding_delegation', timeout=60).content)
        except Exception:
            raise Exception

    # queries all the unbonding of a give validator
    def query_unbonding_from(self, validator):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + validator + '/unbonding_delegations', timeout=60).content)
            responses += results['unbonding_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + validator + '/unbonding_delegations?pagination.key=' + quote(
                        str(pagination)), timeout=60).content)
                responses += results['unbonding_responses']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries params of the mint module.
    def query_mint_params(self):
        endpoint = '/cosmos/mint/v1beta1/params'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries inflation.
    def query_inflation(self):
        endpoint = '/cosmos/mint/v1beta1/inflation'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries annual provisions.
    def query_annual_provisions(self):
        endpoint = '/cosmos/mint/v1beta1/annual_provisions'
        try:
            return json.loads(requests.get(self.lcd + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries a given transaction hash
    def query_tx(self, tx):
        endpoint = '/cosmos/tx/v1beta1/txs/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + tx, timeout=60).content)
        except Exception:
            raise Exception

    # queries abci info.
    def query_abci_info(self):
        endpoint = '/abci_info?'
        try:
            return json.loads(requests.get(self.rpc + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries block by height.
    def query_block(self, height):
        endpoint = '/block?height='
        try:
            return json.loads(requests.get(self.rpc + endpoint + str(height), timeout=60).content)
        except Exception:
            raise Exception

    # queries block results by height.
    def query_block_results(self, height):
        endpoint = '/block_results?height='
        try:
            return json.loads(requests.get(self.rpc + endpoint + str(height), timeout=60).content)
        except Exception:
            raise Exception

    # queries a commit.
    def query_commit(self, height):
        endpoint = '/commit?height='
        try:
            return json.loads(requests.get(self.rpc + endpoint + height, timeout=60).content)
        except Exception:
            raise Exception

    # queries consensus state.
    def query_consensus_state(self):
        endpoint = '/consensus_state?'
        try:
            return json.loads(requests.get(self.rpc + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries dump consensus state.
    def query_dump_consensus_state(self):
        endpoint = '/dump_consensus_state?'
        try:
            return json.loads(requests.get(self.rpc + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries genesis.
    def query_genesis(self):
        endpoint = '/genesis?'
        try:
            return json.loads(requests.get(self.rpc + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries network info.
    def query_net_info(self):
        endpoint = '/net_info?'
        try:
            return json.loads(requests.get(self.rpc + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries the number of unconfirmed transactions.
    def query_num_unconfirmed_txs(self):
        endpoint = '/num_unconfirmed_txs?'
        try:
            return json.loads(requests.get(self.rpc + endpoint, timeout=60).content)
        except Exception:
            raise Exception

    # queries the node status.
    def query_status(self):
        endpoint = '/status?'
        try:
            return json.loads(requests.get(self.rpc + endpoint, timeout=60).content)
        except Exception:
            raise Exception
