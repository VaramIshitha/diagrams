# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _AWS


class _Network(_AWS):
    _type = "network"
    _icon_dir = "resources/aws/network"


class APIGatewayEndpoint(_Network):
    _icon = "api-gateway-endpoint.png"


class APIGateway(_Network):
    _icon = "api-gateway.png"


class AppMesh(_Network):
    _icon = "app-mesh.png"


class ClientVpn(_Network):
    _icon = "client-vpn.png"


class CloudMap(_Network):
    _icon = "cloud-map.png"


class CloudFrontDownloadDistribution(_Network):
    _icon = "cloudfront-download-distribution.png"


class CloudFrontEdgeLocation(_Network):
    _icon = "cloudfront-edge-location.png"


class CloudFrontStreamingDistribution(_Network):
    _icon = "cloudfront-streaming-distribution.png"


class CloudFront(_Network):
    _icon = "cloudfront.png"


class DirectConnect(_Network):
    _icon = "direct-connect.png"


class ElasticLoadBalancing(_Network):
    _icon = "elastic-load-balancing.png"


class ElbApplicationLoadBalancer(_Network):
    _icon = "elb-application-load-balancer.png"


class ElbClassicLoadBalancer(_Network):
    _icon = "elb-classic-load-balancer.png"


class ElbNetworkLoadBalancer(_Network):
    _icon = "elb-network-load-balancer.png"


class Endpoint(_Network):
    _icon = "endpoint.png"


class GlobalAccelerator(_Network):
    _icon = "global-accelerator.png"


class InternetGateway(_Network):
    _icon = "internet-gateway.png"


class Nacl(_Network):
    _icon = "nacl.png"


class NATGateway(_Network):
    _icon = "nat-gateway.png"


class NetworkFirewall(_Network):
    _icon = "network-firewall.png"


class NetworkingAndContentDelivery(_Network):
    _icon = "networking-and-content-delivery.png"


class PrivateSubnet(_Network):
    _icon = "private-subnet.png"


class Privatelink(_Network):
    _icon = "privatelink.png"


class PublicSubnet(_Network):
    _icon = "public-subnet.png"


class Route53HostedZone(_Network):
    _icon = "route-53-hosted-zone.png"


class Route53(_Network):
    _icon = "route-53.png"


class RouteTable(_Network):
    _icon = "route-table.png"


class SiteToSiteVpn(_Network):
    _icon = "site-to-site-vpn.png"


class TransitGateway(_Network):
    _icon = "transit-gateway.png"


class VPCCustomerGateway(_Network):
    _icon = "vpc-customer-gateway.png"


class VPCElasticNetworkAdapter(_Network):
    _icon = "vpc-elastic-network-adapter.png"


class VPCElasticNetworkInterface(_Network):
    _icon = "vpc-elastic-network-interface.png"


class VPCFlowLogs(_Network):
    _icon = "vpc-flow-logs.png"


class VPCPeering(_Network):
    _icon = "vpc-peering.png"


class VPCRouter(_Network):
    _icon = "vpc-router.png"


class VPCTrafficMirroring(_Network):
    _icon = "vpc-traffic-mirroring.png"


class VPC(_Network):
    _icon = "vpc.png"


class VpnConnection(_Network):
    _icon = "vpn-connection.png"


class VpnGateway(_Network):
    _icon = "vpn-gateway.png"


# Aliases

CF = CloudFront
ELB = ElasticLoadBalancing
ALB = ElbApplicationLoadBalancer
CLB = ElbClassicLoadBalancer
NLB = ElbNetworkLoadBalancer
GAX = GlobalAccelerator
