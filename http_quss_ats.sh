#!/bin/sh

# Installing ATS WEB Forward Cache Proxy
# --------------------------------------

su - root
cd /usr/src

// In order to build Apache Traffic Server, a few requirements must be met: 

// gcc / g++ (we have not tested with any other compilers yet)
// PCRE (v3) with the development include files.
// TCL with the development include files.
// Expat with the development include files.

// Ubuntu 12.x - 16.x

apt-get install autoconf automake libtool g++ libssl-dev tcl-dev expat libexpat-dev \
                     libpcre3-dev libcap2 libcap-dev


# Installing a Web Server
# -----------------------

apt-get install apache2
service apache2 start

# Download source code - Release v7.x -- 7.1.4 - 08-2018
# --------------------------------------------------------------
 
wget http://mirror.dkd.de/apache/trafficserver/trafficserver-7.1.4.tar.bz2

# Apache Traffic Server 7.1.4 Validation Files
# --------------------------------------------

wget https://www.apache.org/dist/trafficserver/trafficserver-7.1.4.tar.bz2.asc
wget https://www.apache.org/dist/trafficserver/trafficserver-7.1.4.tar.bz2.md5
wget https://www.apache.org/dist/trafficserver/trafficserver-7.1.4.tar.bz2.sha1

# Validation
# ----------

gpg --verify trafficserver-6.2.0.tar.bz2.asc trafficserver-6.2.0.tar.bz2

>> Signature made Mon Jul 11 18:29:46 2016 CDT using RSA key ID DAE1FE2B

gpg --keyserver pgpkeys.mit.edu --recv-key DAE1FE2B

gpg --fingerprint DAE1FE2B

# Unzip
# -----

tar xvjf trafficserver-7.1.4.tar.bz2
cd trafficserver-7.1.4

# Configure and Compile
# ---------------------

./configure --prefix=/opt/ats
make
make check
make install
export PATH=$PATH:/opt/ats/bin
traffic_server -R 1
trafficserver start
netstat -plnt

# Please Note: Traffic Server is configured as a Reverse Proxy by default
# In order to configure Apache Traffic Server as forward proxy you will 
# have to change thise variables

nano /usr/local/etc/trafficserver/records.config

traffic_ctl config get proxy.config.http.cache.http
traffic_ctl config get proxy.config.reverse_proxy.enabled
traffic_ctl config get proxy.config.url_remap.remap_required
traffic_ctl config get proxy.config.url_remap.pristine_host_hdr

# Reverse Proxy

traffic_ctl config set proxy.config.http.cache.http 1
traffic_ctl config set proxy.config.reverse_proxy.enabled 1
traffic_ctl config set proxy.config.url_remap.remap_required 1
traffic_ctl config set proxy.config.url_remap.pristine_host_hdr 1

# Forword Proxy

traffic_ctl config set proxy.config.reverse_proxy.enabled 0
traffic_ctl config set proxy.config.http.cache.http 1
traffic_ctl config set proxy.config.url_remap.remap_required 0

# As local HTTP-SS Forward Cache Proxy
# Reachable only from localhost
# -----------------------------

traffic_ctl config get proxy.local.incoming_ip_to_bind
traffic_ctl config set roxy.local.incoming_ip_to_bind STRING localhost

traffic_ctl config reload

# Other configuration variables to consider:
# ------------------------------------------
#
# CONFIG proxy.config.http.no_dns_just_forward_to_parent
# CONFIG proxy.config.http.forward.proxy_auth_to_parent
# CONFIG proxy.config.http.insert_squid_x_forwarded_for
#
# 1. DIRECTORY STRUCTURE
# 
#   traffic/ ............... top src dir
#   |-- cop ................ traffic_cop application
#   |-- doc/ ............... generated documentation
#   |-- example/ ........... example plugins
#   |-- install/ ........... installation programs and scripts
#   |-- iocore/ ............ IO core
#   |-- lib/ ...............
#       |-- ts/ ............ Base / core library
#       |-- tsconfig/....... New config parser and library (experimental)
#       |-- records/ ....... library for config files
#   |-- m4/ ................ custom macros for configure.ac
#   |-- mgmt/ .............. Management server and tools (including traffic_manager)
#       |-- cli ............ Command line utilities and API
#   |-- proxy/ ............. HTTP proxy logic
#   |-- test/ .............. functional tests
#   |-- .indent.pro ........ indent profile for coding style
#   |-- emacs-style ........ emacs style definition
#   |-- README ............. intro, links, build info
#   |-- README-EC2 ......... info on EC2 support
#   |-- REVIEWERS .......... (incomplete) list of areas with committer interest
#   |-- LICENSE ............ full license text
#   |-- NOTICE ............. copyright notices
#   |-- configure.ac ....... autoconf configuration
#   `-- Makefile.am ........ top level automake configuration

# Start Traffic Server
#  --------------------

trafficserver start

#  Reload Config
#  -------------

traffic_ctl config reload

#  Stop Traffic Server
#  -------------------

trafficserver stop

#  Config Files
#  ------------

/usr/local/etc/trafficserver/

#  Log Files
#  ---------

/usr/local/var/log/trafficserver

# Size of cache.db
# ----------------

traffic_ctl config get proxy.process.cache.bytes_total
nano /usr/local/etc/trafficserver/storage.config

#  Location
# --------

/usr/local/var/trafficserver

# Accessing the Cache Inspector Utility
# -------------------------------------

# Enable
# ------

traffic_ctl config set proxy.config.http_ui_enabled 1
traffic_ctl config reload

# Check
# -----

traffic_ctl config get proxy.config.http_ui_enabled

# Open GUI
# --------

http://X.X.X.X/myCI

# Checking Cache Capacity
# -----------------------

traffic_ctl config get proxy.process.cache.bytes_total

# Checking Cache Object Size Limit
# --------------------------------

traffic_ctl config get proxy.config.cache.max_doc_size

# Clearing the Cache
# ------------------

trafficserver stop
traffic_server -Cclear
trafficserver start

# Scheduled Updates
# -----------------

traffic_ctl config get proxy.config.update.enabled
nano /usr/local/etc/trafficserver/records.config
traffic_ctl config set proxy.config.update.enabled 1
traffic_ctl config reload

# Ignore Server no-cache Headers
# ------------------------------

traffic_ctl config get proxy.config.http.cache.ignore_server_no_cache
nano /usr/local/etc/trafficserver/records.config
traffic_ctl config set proxy.config.http.cache.ignore_server_no_cache 1
traffic_ctl config reload

# Congestion Control
# ------------------

traffic_ctl config get proxy.config.http.congestion_control.enabled
nano /usr/local/etc/trafficserver/congestion.config




