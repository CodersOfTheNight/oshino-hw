from pytest import fixture, mark

from oshino.core.heart import step
from oshino.config import AgentConfig
from oshino_hw.agent import HWAgent


@fixture
def agent_cfg():
    return AgentConfig({"name": "HWAgentTest", "tag": "test"})


class StubClient(object):
    data = {}

    def event(self, **kwargs):
        self.data = kwargs


class TestAgent(object):

    @mark.asyncio
    async def test_simple_tick(self, agent_cfg, event_loop):
        agents = [(HWAgent(agent_cfg), agent_cfg)]
        stub_client = StubClient()
        await step(stub_client, agents, event_loop)
        assert len(stub_client.data.items()) > 0
