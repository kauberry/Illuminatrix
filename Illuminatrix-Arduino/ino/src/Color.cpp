#include <WString.h>

class Color {
        public:
                int red;
		        int green;
	            int blue;
                int white;
		        String name;

		void initialize(int r, int g, int b, int w) {
			red = r;
			green = g;
			blue = b;
            white = w;
		}
};
