#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;
uniform mat4 modelViewMatrix;


//  Ka, Kd, Ks, S
uniform vec4 matAmbient;
uniform vec4 matDiffuse;
uniform vec4 matSpecular;
uniform float matShininess;


// pos. llum (eye space), Ia,  Id,  Is
uniform vec4 lightPosition;
uniform vec4 lightAmbient;
uniform vec4 lightDiffuse;
uniform vec4 lightSpecular;


vec4 Phong (vec3 N, vec3 L, vec3 V) {
  N = normalize (N);
  V = normalize (V);
  L = normalize (L);
  vec3 R = normalize (2*dot(N, L)*N-L);
  
  float auxR = max(0, dot(R, V));
  float auxN = max(0, dot(N, L));
  float lspec = 0; 
  if (auxN > 0) lspec = pow(auxR, matShininess); 
  
  vec4 f1 = matAmbient * lightAmbient;
  vec4 f2 = matDiffuse * lightDiffuse * auxN;
  vec4 f3 = matSpecular * lightSpecular * lspec;
  
  return f1 + f2 + f3;
}


void main()
{
  vec3 P = (modelViewMatrix*vec4(vertex, 1)).xyz;
  vec3 N = normalMatrix*normal;
  vec3 V = -P;
  vec3 L = lightPosition.xyz-P;
  
  frontColor = Phong(N, V, L);
  gl_Position = modelViewProjectionMatrix*vec4(vertex.xyz, 1.0);
}
