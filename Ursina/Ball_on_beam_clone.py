import ursina as urs
import math
from direct.showbase.ShowBase import ShowBase

class BobClone():

    def __init__(self):

        self.domain_param = dict(
            g = 9.81,  # gravity constant [m/s**2]
            m_ball = 0.5,  # ball mass [kg]
            r_ball = 0.1,  # ball radius [m]
            m_beam = 3.0,  # beam mass [kg]
            l_beam = 2.0,  # beam length [m]
            d_beam = 0.1,  # beam thickness [m]
            c_frict = 0.05,  # viscous friction coefficient [Ns/m]
            ang_offset = 0.0,
        )
        app = urs.Ursina()
        self._anim = dict(canvas=None)
        #self.taskMgr.add(self.update, "update")

        r_ball = self.domain_param["r_ball"]
        l_beam = self.domain_param["l_beam"]
        d_beam = self.domain_param["d_beam"]
        x = float()
        a = float()

        #urs.window.fullscreen = False
        self._anim["canvas"] = urs.window
        self._anim["ball"] = urs.Entity(
            position=urs.Vec3(x, d_beam / 2.0 + r_ball, 0),
            scale=urs.Vec3(r_ball, r_ball, r_ball),
            color=urs.color.red,
            parent=self._anim["canvas"],
        )
        self._anim["beam"] = urs.Entity(
            position=urs.Vec3(0, 0, 0),
            rotation=urs.Vec3(math.cos(a), math.sin(a), 0),
            x=l_beam,
            y=d_beam,
            z=2 * d_beam,
            color=urs.color.green,
            parent=self._anim["canvas"],
        )

    # reset anim
    """
    def _reset_anim(self):

        r_ball = self.domain_param["r_ball"]
        l_beam = self.domain_param["l_beam"]
        d_beam = self.domain_param["d_beam"]

        self._anim["ball"].position = urs.Vec3(float(self.state[0]), math.sin(), 0)

        self._anim["beam"].visible_self = False
        self._anim["beam"] = urs.Entity(
            position=urs.Vec3(0,0,0),
            model='cube',
            x=l_beam,
            y=d_beam,
            z=2 * d_beam,
            color=urs.color.green,
            parent=self._anim["canvas"],
            # scale=(l_beam, d_beam, 2*d_beam)
        )
    

    # init anim
    def _init_anim(self):

        r_ball = self.domain_param["r_ball"]
        l_beam = self.domain_param["l_beam"]
        d_beam = self.domain_param["d_beam"]
        x = float()
        a = float()

        urs.window.fullscreen = False
        self._anim["canvas"] = urs.window
        self._anim["ball"] = urs.Entity(
            position=urs.Vec3(x, d_beam / 2.0 + r_ball, 0),
            scale=urs.Vec3(r_ball, r_ball, r_ball),
            color=urs.color.red,
            parent=self._anim["canvas"],
        )
        self._anim["beam"] = urs.Entity(
            position=urs.Vec3(0, 0, 0),
            rotation=urs.Vec3(math.cos(a), math.sin(a), 0),
            x=l_beam,
            y=d_beam,
            z=2 * d_beam,
            color=urs.color.green,
            parent=self._anim["canvas"],
        )
    """

    # update anim
    def update(self):
        """
        g = self.domain_param["g"]
        m_ball = self.domain_param["m_ball"]
        r_ball = self.domain_param["r_ball"]
        m_beam = self.domain_param["m_beam"]
        l_beam = self.domain_param["l_beam"]
        d_beam = self.domain_param["d_beam"]
        ang_offset = self.domain_param["ang_offset"]
        c_frict = self.domain_param["c_frict"]
        x = float(self.state[0])  # ball position along the beam axis [m]
        a = float(self.state[1])  # angle [rad]

        self._anim["ball"].scale = urs.Vec3(r_ball, r_ball, r_ball)
        self._anim["ball"].position = urs.Vec3(
            math.cos(a) * x - math.sin(a) * (d_beam / 2.0 + r_ball), math.sin(a) * x + math.cos(a) * (d_beam / 2.0 + r_ball), 0
        )

        self._anim["beam"].size = urs.Vec3(l_beam, d_beam, 2 * d_beam)

        self._anim["beam"].rotation_z += float(self.state[3]) * self._dt

        #self._anim["canvas"].
        """

        self._anim["beam"].rotation_z += 1 *1



if __name__ == '__main__':
    #app = urs.Ursina()
    bc = BobClone()
    bc.run()
