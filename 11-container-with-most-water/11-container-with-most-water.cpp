class Solution {
public:
    int maxArea(vector<int>& height) {
        int min_height = height[0];
        int max_height = height[height.size() - 1];
        int min_index = 0;
        int max_index = height.size() - 1;
        
        if(max_height < min_height){
            min_height = max_height;
            min_index = max_index;
            max_height = height[0];
            max_index = 0;
        }
        
        int width = height.size() - 1;
        int max_area = min_height * width;
        
        while(width > 0){
            int index = min_index;
            while(height[index] <= min_height) {
                if(min_index < max_index)
                    index++;
                else
                    index--;
                width--;
                if(width < 1)
                    break;
            }
            if(height[index] > max_height){
                min_height = max_height;
                min_index = max_index;
                max_index = index;
                max_height = height[index];
            }
            else{
                min_index = index;
                min_height = height[index];
            }
            max_area = max(max_area, width * min_height);
        }
        return max_area;
    }
};