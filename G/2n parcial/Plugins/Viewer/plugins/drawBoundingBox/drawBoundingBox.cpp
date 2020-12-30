#include "drawBoundingBox.h"
#include "glwidget.h"
#include <cmath>

void DrawBBox::cleanUp()
{
  glDeleteBuffers(m_size,  &m_coordBufferID);
  glDeleteVertexArrays(1, &m_VAO);
  
  delete m_pVs;
  delete m_pFs;
  delete m_pProgram;
}

DrawBBox::~DrawBBox()
{
  cleanUp();
}

void DrawBBox::onSceneClear()
{
  cleanUp();
}

void DrawBBox::postFrame()
{
  //glPolygonMode( GL_FRONT_AND_BACK, GL_LINE );
  glEnable (GL_BLEND);
  glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
  
  glBindVertexArray(m_VAO);
  vector<Object> &O = scene()->objects();
  m_pProgram->bind();
  QMatrix4x4 MVP = camera()->projectionMatrix() * camera()->modelviewMatrix();
  m_pProgram->setUniformValue("modelViewProjectionMatrix", MVP);
  
  for (Object &o : O) {
    const Box &b = o.boundingBox();
    
    m_pProgram->setUniformValue("boundingBoxMax", b.max());
    m_pProgram->setUniformValue("boundingBoxMin", b.min());
    
    glDrawArrays(GL_TRIANGLES, 0, m_size);
  }
  
  m_pProgram->release();
  
  glDisable(GL_BLEND);
  glBindVertexArray(0);
  //glPolygonMode( GL_FRONT_AND_BACK, GL_FILL );
}


void DrawBBox::onPluginLoad()
{
  vector<float> vertices;
  vector<vector<float>> triangles;
  
  glGenVertexArrays(1, &m_VAO);
  glBindVertexArray(m_VAO);
  
  glGenBuffers(1, &m_coordBufferID);
  
  // 6 planes to visualize the bounding box
  triangles.push_back({ 0,0,0,  1,0,0,  1,1,0 });
  triangles.push_back({ 0,0,0,  1,1,0,  0,1,0 });
  
  triangles.push_back({ 0,0,1,  1,0,1,  1,1,1 });
  triangles.push_back({ 0,0,1,  1,1,1,  0,1,1 });
  
  triangles.push_back({ 0,1,0,  1,1,0,  1,1,1 });
  triangles.push_back({ 0,1,0,  1,1,1,  0,1,1 });
  
  triangles.push_back({ 0,0,0,  1,0,0,  1,0,1 });
  triangles.push_back({ 0,0,0,  1,0,1,  0,0,1 });
  
  triangles.push_back({ 1,0,0,  1,0,1,  1,1,1 });
  triangles.push_back({ 1,0,0,  1,1,0,  1,1,1 });
  
  triangles.push_back({ 0,0,0,  0,0,1,  0,1,1 });
  triangles.push_back({ 0,0,0,  0,1,0,  0,1,1 });
  
  for (vector<float> &V : triangles) for (float f : V) vertices.push_back(f);
  m_size = vertices.size();
  
  glBindBuffer(GL_ARRAY_BUFFER, m_coordBufferID);
  glBufferData(GL_ARRAY_BUFFER, sizeof(float)*vertices.size(), vertices.data(), GL_STATIC_DRAW);
  glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);  // VAO
  glEnableVertexAttribArray(0);
  
  m_pVs = new QGLShader(QGLShader::Vertex, this);
  m_pVs->compileSourceFile(":/drawBB.vert");
  cout << "VS log: " << m_pVs->log().toStdString() << endl;
  
  m_pFs = new QGLShader(QGLShader::Fragment, this);
  m_pFs->compileSourceFile(":/drawBB.frag");
  cout << "FS log: " << m_pFs->log().toStdString() << endl;
  
  m_pProgram = new QGLShaderProgram(this);
  m_pProgram->addShader(m_pVs);
  m_pProgram->addShader(m_pFs);
  m_pProgram->link();
  cout << "Link log: " << m_pProgram->log().toStdString() << endl;
}

#if QT_VERSION < 0x050000
Q_EXPORT_PLUGIN2(drawBoundingBox, DrawBBox)   // plugin name, plugin class
#endif



