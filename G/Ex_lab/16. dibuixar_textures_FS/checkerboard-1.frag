#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

const vec4 grey = vec4(vec3(0.8), 1);
const vec4 black = vec4(vec3(0), 1);

void main() {
  float p = 1.0/8;
  int x = int(mod(vtexCoord.x/p, 2));
  int y = int(mod(vtexCoord.y/p, 2));
  
  if (x==y) fragColor=grey;
  else fragColor=black;
}
