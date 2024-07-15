## if 초기화 구문 

- c++ 17로 오면서 if문 초기화를 할 수 있다.


````c++

bool PacketProcess::ProcessPacket(const char* packetData)
{
    auto packetHeader = (pkt::PkHeader*)packetData;

    if(auto packetHandler = handlers.find(packetHeader->id); packetHandler != handlers.end())
    {
        p_handler->second->Process(packetData)

        return true;
    }

    return false;
}
````


````c++
bool PacketProcessor::ProcessProxyPacket(const char* p_pkt_data)
{
    auto p_header = (pkt::PktHeader*)p_pkt_data;

    // 핸들러를 찾기 위해 초기화 및 조건 분리
    auto p_handler = proxy_handlers_.find(p_header->id_);
    if (p_handler != proxy_handlers_.end()) 
    {
        p_handler->second->Process(p_pkt_data);
        return true;
    }

    return false;
}
````