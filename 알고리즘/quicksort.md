````c++
#include <iostream>
#include <vector>

using namespace std;

/*
* 시간 복잡도
	- NlogN
	- N개의 partion으로 분할하는 횟수, 그리고 logN은 4개의 공간을 => 2, 2로 나누는 행위 logN
	//지수 < - > 로그
*/

void Swap(vector<int>& v, int start, int end)
{
	int tmp = v[start];
	v[start] = v[end];
	v[end] = tmp;
}

int Partition(vector<int>& v, int start, int end)
{
	// 가운데를 pivot으로 정함 
	int pivot = v[(start + end) / 2];

	while (start <= end)
	{
		// pivot보다 작다면 무시하고 지나감
		while (v[start] < pivot)
		{
			start++;
		}

		// pivot보다 크다면 무시하고 지나감
		while (v[end] > pivot)
		{
			end--;  // 여기서는 end를 감소시켜야 합니다.
		}

		// start와 end가 교차하지 않았을 때 교환 수행
		if (start <= end)
		{
			Swap(v, start, end);
			start++;
			end--;
		}
	}
	return start;
}

void QuickSort(vector<int>& v, int start, int end)
{
	// QuickSort는 pivot을 고른다.
	if (start < end)
	{
		// 배열을 파티셔닝하고 pivot의 위치를 가져옴
		int pivotPos = Partition(v, start, end);

		// pivot 획득 후 왼, 오 다시 퀵소트 정렬 시행 
		QuickSort(v, start, pivotPos - 1);
		QuickSort(v, pivotPos, end);
	}
}

int main()
{
	vector<int> v{ 1, 7, 4, 3, 2, 99, 22 };
	int size = v.size();

	QuickSort(v, 0, size - 1);  // 여기서는 size - 1로 수정해야 합니다.

	for (auto& number : v)
	{
		cout << number << " ";
	}
	cout << endl;

	return 0;
}
````