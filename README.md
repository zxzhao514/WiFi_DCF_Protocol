# WiFi_DCF_Protocol

DCF is a contention-based multiple access scheme (aka. best effort access). The scheme adopts carrier
sense multiple access with collision avoidance (CSMA/CA) protocol. The CSMA/CA scheme is described
as below.
1) A station that has frames ready to send much first sense the channel to find out whether it is currently
empty or occupied by the frames transmitted by other stations.
2) If the channel is detected as busy status nodes will perform the defer process.
3) If the channel is detected as free for a period of inter-frame space (IFS) duration, the back-off (BO)
counter start counting down and the node whose BO counter goes to zero starts to transmit.
4) After transmission, the transmission node will wait for an acknowledgement (AKC) message from destination node. If ACK is received the transmission is completed and the node will content for next frame
transmission if the traffic is assumed to be saturated meaning there are infinite number of frame to be
sent. If it not received it within a given duration (time out), collision is assumed the increase the retrials
counter and perform defer process.
5) During the defer process, the node will be randomly assigned an integer between [0, 2
n − 1] where n is
the number of retrials.
