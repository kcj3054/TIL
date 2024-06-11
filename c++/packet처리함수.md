````c++
#include <iostream>
#include <thread>
#include <concurrent_queue.h>

using namespace std;


struct Packet
{

};

// test위한 class 
class PacketProcessor
{
public:
	PacketProcessor() {}
	~PacketProcessor() { Stop(); }

public:
	void Init();
	void Run();
	void WorkerThread();
	void ProcessPacket();
	void Stop();

	void ProcessPacket(Packet& p);

public:
	std::jthread worker_thread;
	std::atomic<bool> is_run = false;
	Concurrency::concurrent_queue<Packet> test_packet;
};



int main()
{
	//todo 

	return 0;
}

void PacketProcessor::Init()
{
}

void PacketProcessor::Run()
{
	is_run = true;
	worker_thread = std::jthread([this] {WorkerThread();});
	
}

void PacketProcessor::WorkerThread()
{
	while (is_run)
	{
		Packet packet;
		if (!test_packet.try_pop(packet))
		{
			// todo packet 처리 
			ProcessPacket(packet);
		}
		else
		{
			std::this_thread::sleep_for(std::chrono::milliseconds(1));
		}
	}
}

void PacketProcessor::Stop()
{
	is_run = false;
}

void PacketProcessor::ProcessPacket(Packet& p)
{
	cout << "처리" << endl;
}

````