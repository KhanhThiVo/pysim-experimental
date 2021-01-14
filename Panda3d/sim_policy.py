# Copyright (c) 2020, Fabio Muratore, Honda Research Institute Europe GmbH, and
# Technical University of Darmstadt.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of Fabio Muratore, Honda Research Institute Europe GmbH,
#    or Technical University of Darmstadt, nor the names of its contributors may
#    be used to endorse or promote products derived from this software without
#    specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL FABIO MURATORE, HONDA RESEARCH INSTITUTE EUROPE GMBH,
# OR TECHNICAL UNIVERSITY OF DARMSTADT BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Simulate (with animation) a rollout in an environment.
"""
from prettyprinter import pprint

import pyrado
from pyrado.domain_randomization.utils import print_domain_params
from pyrado.environment_wrappers.domain_randomization import remove_all_dr_wrappers
from pyrado.logger.experiment import ask_for_experiment
from pyrado.sampling.rollout import rollout, after_rollout_query
from pyrado.utils.argparser import get_argparser
from pyrado.utils.experiments import load_experiment
from pyrado.utils.input_output import print_cbt
from pyrado.utils.data_types import RenderMode

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

from pyrado.environments.pysim.ball_on_beam import BallOnBeamSim



if __name__ == "__main__":
    # Parse command line arguments
    args = get_argparser().parse_args()

    # Get the experiment's directory to load from
    ex_dir = ask_for_experiment() if args.dir is None else args.dir

    # Load the environment and the policy
    env, policy, kwout = load_experiment(ex_dir, args)

    # Override the time step size if specified
    if args.dt is not None:
        env.dt = args.dt

    if args.verbose:
        print("Hyper-parameters of the experiment")
        pprint(kwout.get("hparams", "No hyper-parameters found!"))

    if args.remove_dr_wrappers:
        env = remove_all_dr_wrappers(env, verbose=True)

    # Use the environments number of steps in case of the default argument (inf)
    max_steps = env.max_steps if args.max_steps == pyrado.inf else args.max_steps
    print("0")
    # Simulate
    class Simulation(ShowBase):
        def __init__(self):
            ShowBase.__init__(self)
            self.done = False
            self.state = None
            self.param = None
            print("a")
            self.ro = rollout(
                env,
                policy,
                render_mode=RenderMode(text=args.verbose, video=args.animation),
                eval=True,
                max_steps=max_steps,
                stop_on_done=not args.relentless,
                reset_kwargs=dict(domain_param=self.param, init_state=self.state),
            )
            print("hoi")
            print_domain_params(env.domain_param)
            print_cbt(f"Return: {self.ro.undiscounted_return()}", "g", bright=True)
            self.done, self.state, self.param = after_rollout_query(env, policy, self.ro)
            print("1")
            self.bob = BallOnBeamSim(2)
            print("2")
            self.pos, self.r_ball,self.a,self.l_beam,self.d_beam = self.bob._init_anim()
            print("3")
            self.ball = self.loader.loadModel("my_models/ball")
            self.ball.reparentTo(self.render)
            self.ball.setPos(self.pos)
            self.box = self.loader.loadModel("my_models/box")
            self.box.reparentTo(self.render)
            self.box.setPos(0,0,0)
            self.box.setScale(self.l_beam,self.d_beam,2*self.d_beam)
            self.camera.setPos(0,-10,0)
    
    simulation = Simulation()
    simulation.run()
            
            
            
            
