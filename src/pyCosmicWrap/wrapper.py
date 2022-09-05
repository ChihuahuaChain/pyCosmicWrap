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
    def __init__(self, lcd: str, rpc: str, udenom: str):
        self.lcd = lcd
        self.rpc = rpc
        self.udenom = udenom

    # queries the balance of all coins for a single account.
    def query_balances(self, address: str):
        responses = []
        endpoint = '/cosmos/bank/v1beta1/balances/'
        try:
            results = json.loads(requests.get(self.lcd + endpoint + address).content)
            responses += results['balances']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + '?pagination.key=' + quote(str(pagination))).content)
                responses += results['balances']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries the balance of a given udenom for a single account.
    def query_balances_by_udenom(self, address, udenom):
        endpoint = '/cosmos/bank/v1beta1/balances/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/by_denom?denom=' + udenom).content)
        except Exception:
            raise Exception

    # queries the total supply of all coins.
    def query_supply(self):
        endpoint = '/cosmos/bank/v1beta1/supply'
        try:
            return json.loads(requests.get(self.lcd + endpoint).content)
        except Exception:
            raise Exception

    # queries the total supply of a given udenom.
    def query_supply_by_udenom(self, udenom):
        udenom = self.udenom if udenom is None else udenom
        endpoint = '/cosmos/bank/v1beta1/supply/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + udenom).content)
        except Exception:
            raise Exception

    # queries the community pool coins.
    def query_community_pool(self):
        endpoint = '/cosmos/distribution/v1beta1/community_pool'
        try:
            return json.loads(requests.get(self.lcd + endpoint).content)
        except Exception:
            raise Exception

    # queries the total rewards accrued by every validator.
    def query_rewards(self, address):
        endpoint = '/cosmos/distribution/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/rewards').content)
        except Exception:
            raise Exception

    # queries the total rewards accrued by a given validator.
    def query_rewards_by_validator(self, address, validator):
        endpoint = '/cosmos/distribution/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/rewards/' + validator).content)
        except Exception:
            raise Exception

    # queries the validators of a delegator.
    def query_delegator_validators(self, address):
        endpoint = '/cosmos/distribution/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/validators').content)
        except Exception:
            raise Exception

    # queries withdraw address of a delegator.
    def query_withdraw_address(self, address):
        endpoint = '/cosmos/distribution/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/withdraw_address').content)
        except Exception:
            raise Exception

    # queries params of the distribution module.
    def query_distribution_params(self):
        endpoint = '/cosmos/distribution/v1beta1/params'
        try:
            return json.loads(requests.get(self.lcd + endpoint).content)
        except Exception:
            raise Exception

    # queries accumulated commission for a validator.
    def query_commission(self, validator):
        endpoint = '/cosmos/distribution/v1beta1/validators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + validator + '/commission').content)
        except Exception:
            raise Exception

    # queries accumulated rewards for a validator.
    def query_outstanding_rewards(self, address):
        endpoint = '/cosmos/distribution/v1beta1/validators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/outstanding_rewards').content)
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
            results = json.loads(requests.get(self.lcd + endpoint).content)
            responses += results['proposals']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + '?pagination.key=' + quote(str(pagination))).content)
                responses += results['proposals']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries a proposal by a given id
    def query_proposals_by_id(self, proposal_id):
        endpoint = '/cosmos/gov/v1beta1/proposals/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + str(proposal_id)).content)
        except Exception:
            raise Exception

    # queries the tally of a proposal by a given id
    def query_tally(self, proposal_id):
        endpoint = '/cosmos/gov/v1beta1/proposals/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + str(proposal_id) + '/tally').content)
        except Exception:
            raise Exception

    # queries the votes of a proposal by a given id
    def query_votes(self, proposal_id):
        responses = []
        endpoint = '/cosmos/gov/v1beta1/proposals/'
        try:
            results = json.loads(requests.get(self.lcd + endpoint + str(proposal_id) + '/votes').content)
            responses += results['votes']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + str(proposal_id) + '/votes' + '?pagination.key=' + quote(
                        str(pagination))).content)
                responses += results['votes']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries a voter of a given proposal.
    def query_votes_by_address(self, proposal_id, address):
        endpoint = '/cosmos/gov/v1beta1/proposals/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + str(proposal_id) + '/votes/' + address).content)
        except Exception:
            raise Exception

    # queries the slashing parameters
    def query_slashing_params(self):
        endpoint = '/cosmos/slashing/v1beta1/params'
        try:
            return json.loads(requests.get(self.lcd + endpoint).content)
        except Exception:
            raise Exception

    # queries delegations of a given address
    def query_delegations_by_address(self, address):
        endpoint = '/cosmos/staking/v1beta1/delegations/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + address).content)
            responses += results['delegation_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + address + '?pagination.key=' + quote(str(pagination))).content)
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
            results = json.loads(requests.get(self.lcd + endpoint + address + '/redelegations').content)
            responses += results['redelegation_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + address + '/redelegations?pagination.key=' + quote(str(pagination))).content)
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
            results = json.loads(requests.get(self.lcd + endpoint + address + '/unbonding_delegations').content)
            responses += results['unbonding_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + address + '/unbonding_delegations?pagination.key=' + quote(
                        str(pagination))).content)
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
            results = json.loads(requests.get(self.lcd + endpoint + address + '/validators').content)
            responses += results['validators']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + address + '/validators?pagination.key=' + quote(str(pagination))).content)
                responses += results['validators']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries delegator data of a given address on a given validator
    def query_delegator_data_by_validator(self, address, validator):
        endpoint = '/cosmos/staking/v1beta1/delegators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address + '/validators/' + validator).content)
        except Exception:
            raise Exception

    # queries staking parameters
    def query_staking_params(self):
        endpoint = '/cosmos/staking/v1beta1/params'
        try:
            return json.loads(requests.get(self.lcd + endpoint).content)
        except Exception:
            raise Exception

    # queries staking pool
    def query_staking_pool(self):
        endpoint = '/cosmos/staking/v1beta1/pool'
        try:
            return json.loads(requests.get(self.lcd + endpoint).content)
        except Exception:
            raise Exception

    # queries all the validators
    def query_all_validators(self):
        endpoint = '/cosmos/staking/v1beta1/validators'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint).content)
            responses += results['validators']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(
                    requests.get(self.lcd + endpoint + '?pagination.key=' + quote(str(pagination))).content)
                responses += results['validators']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries a validator by a given address
    def query_validator_by_address(self, address):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + address).content)
        except Exception:
            raise Exception

    # queries delegators of a given validator
    def query_delegators(self, validator):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + validator + '/delegations').content)
            responses += results['delegation_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + validator + '/delegations?pagination.key=' + quote(str(pagination))).content)
                responses += results['delegation_responses']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception

    # queries a validator for a specific delegator address
    def query_delegators_by_address(self, validator, address):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        try:
            return json.loads(requests.get(self.lcd + endpoint + validator + '/delegations/' + address).content)
        except Exception:
            raise Exception

    # queries a validator for a specific unbonding address
    def query_validator_unbonding_by_address(self, validator, address):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        try:
            return json.loads(requests.get(
                self.lcd + endpoint + validator + '/delegations/' + address + '/unbonding_delegation').content)
        except Exception:
            raise Exception

    # queries all the unbonding of a give validator
    def query_unbonding_from(self, validator):
        endpoint = '/cosmos/staking/v1beta1/validators/'
        responses = []
        try:
            results = json.loads(requests.get(self.lcd + endpoint + validator + '/unbonding_delegations').content)
            responses += results['unbonding_responses']
            pagination = results['pagination']['next_key']
            while pagination is not None:
                results = json.loads(requests.get(
                    self.lcd + endpoint + validator + '/unbonding_delegations?pagination.key=' + quote(
                        str(pagination))).content)
                responses += results['unbonding_responses']
                pagination = results['pagination']['next_key']
            return responses
        except Exception:
            raise Exception
