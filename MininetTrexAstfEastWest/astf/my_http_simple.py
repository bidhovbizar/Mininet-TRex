from trex.astf.api import *
import argparse


class Prof1():
    def __init__(self):
        pass

    def get_profile(self, tunables, **kwargs):
        parser = argparse.ArgumentParser(description='Argparser for {}'.format(os.path.basename(__file__)), 
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        args = parser.parse_args(tunables)
        # ip generator
        ip_gen_c = ASTFIPGenDist(ip_range=["10.0.0.10", "10.0.0.10"], distribution="seq")
        ip_gen_s = ASTFIPGenDist(ip_range=["10.0.0.13", "10.0.0.13"], distribution="seq")
        ip_gen = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s)

        return ASTFProfile(default_ip_gen=ip_gen,
                            cap_list=[ASTFCapInfo(file="../avl/delay_10_http_browsing_0.pcap",
                            cps=2.776)])


def register():
    return Prof1()
