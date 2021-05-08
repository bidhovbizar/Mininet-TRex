#Run this to ensure your system is cleaned for running any of the setup and run scripts
echo "cleaning previous mininet"
mn -c
echo
#Sometimes a controller may occupy port 6653 which is due to some race around condition which I am unable to sort. So the best practice is to kill what ever process currently uses the port using fuser
echo "closing process using port 6653/tcp"
fuser -k 6653/tcp
echo ""
#Cleanup the Trex link and port to switch s1 which ensures it cleans up any previous veth ports
echo "cleaning Trex in root namespace"
bash ./cleanupTrexMininet.sh
