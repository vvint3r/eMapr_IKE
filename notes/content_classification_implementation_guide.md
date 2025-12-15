# Content Classification Implementation Guide
## With Practical Templates and Code Examples

---

## 1. TAB-DELIMITED TAXONOMY TEMPLATE

### 1.1 Standard Hierarchical Format (6-Level)
```tsv
UNIQUE_ID	PARENT_ID	NAME	LEVEL_1	LEVEL_2	LEVEL_3	LEVEL_4	LEVEL_5	LEVEL_6	CONTENT_TYPE	DEPTH	CONTEXT	PURPOSE	TAGS
BUS001	NULL	Business & Economy	Business & Economy						C	F	S	Educational	business,economy,foundational
BUS002	BUS001	Marketing	Business & Economy	Marketing					M	F	S,A	Educational	marketing,strategy
BUS003	BUS002	Digital Marketing	Business & Economy	Marketing	Digital Marketing				M	I	A,O	Informational	digital,online,marketing
BUS004	BUS003	Search Marketing	Business & Economy	Marketing	Digital Marketing	Search Marketing			T	I	O,R	Transactional	seo,sem,ppc
BUS005	BUS004	SEO	Business & Economy	Marketing	Digital Marketing	Search Marketing	SEO		T	A	O	Implementation	organic,search,optimization
BUS006	BUS005	Technical SEO	Business & Economy	Marketing	Digital Marketing	Search Marketing	SEO	Technical SEO	Ta	E	O	Implementation	crawling,indexing,technical
```

### 1.2 Multi-Dimensional Classification Template
```tsv
ID	HIERARCHY_PATH	PRIMARY_DIM	SECONDARY_DIM	TERTIARY_DIM	METADATA	QUALITY_SCORE	STATUS
001	/Business/Marketing/Digital/SEO	Domain:Business	Type:Technical	Context:Operational	{"audience":"intermediate","update_freq":"monthly"}	85	Active
002	/Technology/AI/ML/DeepLearning	Domain:Technology	Type:Methodological	Context:Analytical	{"audience":"advanced","update_freq":"weekly"}	92	Active
003	/Finance/Banking/Retail/Digital	Domain:Finance	Type:Operational	Context:Strategic	{"audience":"executive","update_freq":"quarterly"}	78	Review
```

---

## 2. PYTHON IMPLEMENTATION

### 2.1 Content Classification Class
```python
import pandas as pd
import json
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import hashlib

class ContentClassificationSystem:
    """
    Comprehensive content classification and categorization system
    """
    
    def __init__(self):
        self.taxonomy = {}
        self.content_items = {}
        self.relationships = {}
        self.metadata_schema = self._initialize_metadata_schema()
        
    def _initialize_metadata_schema(self) -> Dict:
        """Initialize the metadata schema for content items"""
        return {
            'required_fields': [
                'content_id', 'title', 'domain', 'category', 
                'content_type', 'created_date'
            ],
            'dimensions': {
                'hierarchical': ['domain', 'category', 'subcategory', 
                               'topic', 'subtopic', 'element'],
                'content_type': ['conceptual', 'methodological', 'technical', 
                                'operational', 'tactical'],
                'knowledge_depth': ['foundational', 'intermediate', 
                                   'advanced', 'expert'],
                'application_context': ['strategic', 'analytical', 
                                       'operational', 'reporting']
            },
            'quality_metrics': {
                'accuracy': (0, 100),
                'completeness': (0, 100),
                'relevance': (0, 100),
                'trust_score': (0, 100)
            }
        }
    
    def generate_content_id(self, domain: str, category: str, 
                           subcategory: str) -> str:
        """
        Generate unique content ID based on classification
        Format: DOMAIN-CATEGORY-SUBCATEGORY-YYYY-SEQUENTIAL
        """
        domain_code = domain[:3].upper()
        category_code = category[:3].upper()
        subcategory_code = subcategory[:3].upper()
        year = datetime.now().year
        
        # Generate sequential number
        seq_key = f"{domain_code}-{category_code}-{subcategory_code}-{year}"
        if seq_key not in self.taxonomy:
            self.taxonomy[seq_key] = 0
        self.taxonomy[seq_key] += 1
        
        sequential = str(self.taxonomy[seq_key]).zfill(5)
        
        return f"{domain_code}-{category_code}-{subcategory_code}-{year}-{sequential}"
    
    def classify_content(self, content: Dict) -> Dict:
        """
        Classify content based on multi-dimensional framework
        """
        classification = {
            'content_id': self.generate_content_id(
                content.get('domain', 'UNK'),
                content.get('category', 'UNK'),
                content.get('subcategory', 'UNK')
            ),
            'timestamp': datetime.now().isoformat(),
            'hierarchy': self._build_hierarchy(content),
            'dimensions': self._classify_dimensions(content),
            'metadata': self._extract_metadata(content),
            'quality_score': self._calculate_quality_score(content),
            'relationships': self._identify_relationships(content)
        }
        
        # Store in system
        self.content_items[classification['content_id']] = classification
        
        return classification
    
    def _build_hierarchy(self, content: Dict) -> List[str]:
        """Build hierarchical path for content"""
        hierarchy = []
        for level in self.metadata_schema['dimensions']['hierarchical']:
            if level in content and content[level]:
                hierarchy.append(content[level])
        return hierarchy
    
    def _classify_dimensions(self, content: Dict) -> Dict:
        """Classify content across multiple dimensions"""
        dimensions = {}
        
        # Content Type Classification
        content_text = content.get('text', '').lower()
        if any(word in content_text for word in ['theory', 'principle', 'concept']):
            dimensions['content_type'] = 'conceptual'
        elif any(word in content_text for word in ['method', 'framework', 'approach']):
            dimensions['content_type'] = 'methodological'
        elif any(word in content_text for word in ['tool', 'software', 'platform']):
            dimensions['content_type'] = 'technical'
        elif any(word in content_text for word in ['process', 'workflow', 'procedure']):
            dimensions['content_type'] = 'operational'
        elif any(word in content_text for word in ['metric', 'kpi', 'measurement']):
            dimensions['content_type'] = 'tactical'
        else:
            dimensions['content_type'] = 'general'
        
        # Knowledge Depth Classification
        complexity_indicators = {
            'foundational': ['basic', 'introduction', 'fundamental', 'beginner'],
            'intermediate': ['practical', 'applied', 'standard', 'common'],
            'advanced': ['complex', 'specialized', 'expert', 'advanced'],
            'expert': ['cutting-edge', 'research', 'innovation', 'novel']
        }
        
        for depth, indicators in complexity_indicators.items():
            if any(ind in content_text for ind in indicators):
                dimensions['knowledge_depth'] = depth
                break
        
        # Application Context
        context_indicators = {
            'strategic': ['strategy', 'executive', 'leadership', 'vision'],
            'analytical': ['analysis', 'research', 'investigate', 'insight'],
            'operational': ['operation', 'execution', 'implement', 'daily'],
            'reporting': ['report', 'dashboard', 'communicate', 'present']
        }
        
        dimensions['application_context'] = []
        for context, indicators in context_indicators.items():
            if any(ind in content_text for ind in indicators):
                dimensions['application_context'].append(context)
        
        return dimensions
    
    def _extract_metadata(self, content: Dict) -> Dict:
        """Extract comprehensive metadata from content"""
        metadata = {
            'created_date': content.get('created_date', datetime.now().isoformat()),
            'modified_date': content.get('modified_date', datetime.now().isoformat()),
            'author': content.get('author', 'unknown'),
            'version': content.get('version', '1.0'),
            'language': content.get('language', 'en'),
            'format': content.get('format', 'text'),
            'word_count': len(content.get('text', '').split()),
            'tags': self._generate_tags(content),
            'audience': self._identify_audience(content)
        }
        return metadata
    
    def _generate_tags(self, content: Dict) -> List[str]:
        """Generate relevant tags for content"""
        tags = []
        
        # Extract from hierarchy
        tags.extend([h.lower().replace(' ', '_') 
                    for h in self._build_hierarchy(content)])
        
        # Add dimension tags
        dimensions = self._classify_dimensions(content)
        tags.append(f"type:{dimensions.get('content_type', 'unknown')}")
        tags.append(f"depth:{dimensions.get('knowledge_depth', 'unknown')}")
        
        # Extract keywords (simplified version)
        text = content.get('text', '')
        # In production, use NLP libraries for better keyword extraction
        keywords = [word.lower() for word in text.split() 
                   if len(word) > 5][:10]
        tags.extend(keywords)
        
        return list(set(tags))  # Remove duplicates
    
    def _identify_audience(self, content: Dict) -> Dict:
        """Identify target audience for content"""
        audience = {
            'expertise_level': 'general',
            'roles': [],
            'departments': [],
            'industries': []
        }
        
        text = content.get('text', '').lower()
        
        # Expertise level
        if any(word in text for word in ['advanced', 'expert', 'senior']):
            audience['expertise_level'] = 'expert'
        elif any(word in text for word in ['intermediate', 'professional']):
            audience['expertise_level'] = 'intermediate'
        elif any(word in text for word in ['beginner', 'basic', 'introduction']):
            audience['expertise_level'] = 'beginner'
        
        # Roles
        role_indicators = {
            'executive': ['ceo', 'cto', 'executive', 'leadership'],
            'manager': ['manager', 'supervisor', 'lead', 'head'],
            'analyst': ['analyst', 'specialist', 'researcher'],
            'developer': ['developer', 'engineer', 'programmer']
        }
        
        for role, indicators in role_indicators.items():
            if any(ind in text for ind in indicators):
                audience['roles'].append(role)
        
        return audience
    
    def _calculate_quality_score(self, content: Dict) -> float:
        """Calculate overall quality score for content"""
        scores = []
        
        # Completeness check
        required_fields = self.metadata_schema['required_fields']
        completeness = sum(1 for field in required_fields 
                         if field in content and content[field]) / len(required_fields)
        scores.append(completeness * 100)
        
        # Content depth (word count as proxy)
        word_count = len(content.get('text', '').split())
        if word_count > 1000:
            depth_score = 100
        elif word_count > 500:
            depth_score = 75
        elif word_count > 200:
            depth_score = 50
        else:
            depth_score = 25
        scores.append(depth_score)
        
        # Metadata richness
        metadata = self._extract_metadata(content)
        metadata_score = len([v for v in metadata.values() 
                            if v and v != 'unknown']) / len(metadata) * 100
        scores.append(metadata_score)
        
        return sum(scores) / len(scores)
    
    def _identify_relationships(self, content: Dict) -> Dict:
        """Identify relationships with other content"""
        relationships = {
            'prerequisites': [],
            'related': [],
            'follows': [],
            'references': []
        }
        
        # Simplified relationship identification
        # In production, use graph databases and ML for better relationship mapping
        
        content_id = content.get('content_id', '')
        domain = content.get('domain', '')
        category = content.get('category', '')
        
        # Find related content in same category
        for item_id, item in self.content_items.items():
            if item_id != content_id:
                if item.get('hierarchy', [])[0:2] == [domain, category]:
                    relationships['related'].append(item_id)
        
        return relationships
    
    def export_taxonomy_tsv(self, filepath: str):
        """Export taxonomy to tab-delimited file"""
        data = []
        
        for content_id, content in self.content_items.items():
            hierarchy = content.get('hierarchy', [])
            dimensions = content.get('dimensions', {})
            metadata = content.get('metadata', {})
            
            row = {
                'UNIQUE_ID': content_id,
                'LEVEL_1': hierarchy[0] if len(hierarchy) > 0 else '',
                'LEVEL_2': hierarchy[1] if len(hierarchy) > 1 else '',
                'LEVEL_3': hierarchy[2] if len(hierarchy) > 2 else '',
                'LEVEL_4': hierarchy[3] if len(hierarchy) > 3 else '',
                'LEVEL_5': hierarchy[4] if len(hierarchy) > 4 else '',
                'LEVEL_6': hierarchy[5] if len(hierarchy) > 5 else '',
                'CONTENT_TYPE': dimensions.get('content_type', ''),
                'KNOWLEDGE_DEPTH': dimensions.get('knowledge_depth', ''),
                'APPLICATION_CONTEXT': ','.join(dimensions.get('application_context', [])),
                'TAGS': ','.join(metadata.get('tags', [])),
                'QUALITY_SCORE': content.get('quality_score', 0),
                'CREATED_DATE': metadata.get('created_date', ''),
                'MODIFIED_DATE': metadata.get('modified_date', '')
            }
            data.append(row)
        
        df = pd.DataFrame(data)
        df.to_csv(filepath, sep='\t', index=False)
        print(f"Taxonomy exported to {filepath}")
    
    def import_taxonomy_tsv(self, filepath: str):
        """Import taxonomy from tab-delimited file"""
        df = pd.read_csv(filepath, sep='\t')
        
        for _, row in df.iterrows():
            content = {
                'content_id': row['UNIQUE_ID'],
                'domain': row['LEVEL_1'],
                'category': row['LEVEL_2'] if pd.notna(row['LEVEL_2']) else None,
                'subcategory': row['LEVEL_3'] if pd.notna(row['LEVEL_3']) else None,
                'topic': row['LEVEL_4'] if pd.notna(row['LEVEL_4']) else None,
                'subtopic': row['LEVEL_5'] if pd.notna(row['LEVEL_5']) else None,
                'element': row['LEVEL_6'] if pd.notna(row['LEVEL_6']) else None,
                'content_type': row['CONTENT_TYPE'],
                'knowledge_depth': row['KNOWLEDGE_DEPTH'],
                'created_date': row['CREATED_DATE']
            }
            
            self.classify_content(content)
        
        print(f"Imported {len(df)} items from {filepath}")

# Usage Example
if __name__ == "__main__":
    # Initialize system
    classifier = ContentClassificationSystem()
    
    # Example content classification
    sample_content = {
        'title': 'Advanced SEO Technical Implementation Guide',
        'text': 'This advanced guide covers technical SEO implementation including crawling, indexing, and core web vitals optimization...',
        'domain': 'Business & Economy',
        'category': 'Marketing',
        'subcategory': 'Digital Marketing',
        'topic': 'Search Marketing',
        'subtopic': 'SEO',
        'element': 'Technical SEO',
        'author': 'John Doe',
        'created_date': '2024-01-15'
    }
    
    # Classify the content
    classification_result = classifier.classify_content(sample_content)
    print(json.dumps(classification_result, indent=2))
    
    # Export to TSV
    classifier.export_taxonomy_tsv('content_taxonomy.tsv')
```

---

## 3. SQL SCHEMA FOR CONTENT CLASSIFICATION

### 3.1 Database Schema
```sql
-- Main taxonomy hierarchy table
CREATE TABLE taxonomy_hierarchy (
    id SERIAL PRIMARY KEY,
    unique_id VARCHAR(50) UNIQUE NOT NULL,
    parent_id VARCHAR(50),
    name VARCHAR(255) NOT NULL,
    level_1 VARCHAR(255),
    level_2 VARCHAR(255),
    level_3 VARCHAR(255),
    level_4 VARCHAR(255),
    level_5 VARCHAR(255),
    level_6 VARCHAR(255),
    hierarchy_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES taxonomy_hierarchy(unique_id)
);

-- Content classification table
CREATE TABLE content_classification (
    id SERIAL PRIMARY KEY,
    content_id VARCHAR(50) UNIQUE NOT NULL,
    taxonomy_id VARCHAR(50) NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    content_type VARCHAR(50),
    knowledge_depth VARCHAR(50),
    application_context TEXT[],
    primary_purpose VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (taxonomy_id) REFERENCES taxonomy_hierarchy(unique_id)
);

-- Multi-dimensional classification
CREATE TABLE classification_dimensions (
    id SERIAL PRIMARY KEY,
    content_id VARCHAR(50) NOT NULL,
    dimension_type VARCHAR(50) NOT NULL,
    dimension_value VARCHAR(100) NOT NULL,
    confidence_score DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES content_classification(content_id)
);

-- Content metadata
CREATE TABLE content_metadata (
    id SERIAL PRIMARY KEY,
    content_id VARCHAR(50) NOT NULL,
    author VARCHAR(255),
    version VARCHAR(20),
    language VARCHAR(10),
    format VARCHAR(50),
    word_count INTEGER,
    quality_score DECIMAL(5,2),
    trust_score DECIMAL(5,2),
    created_date TIMESTAMP,
    modified_date TIMESTAMP,
    expiry_date TIMESTAMP,
    metadata_json JSONB,
    FOREIGN KEY (content_id) REFERENCES content_classification(content_id)
);

-- Tags and keywords
CREATE TABLE content_tags (
    id SERIAL PRIMARY KEY,
    content_id VARCHAR(50) NOT NULL,
    tag_type VARCHAR(50),
    tag_value VARCHAR(255) NOT NULL,
    relevance_score DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES content_classification(content_id)
);

-- Content relationships
CREATE TABLE content_relationships (
    id SERIAL PRIMARY KEY,
    source_content_id VARCHAR(50) NOT NULL,
    target_content_id VARCHAR(50) NOT NULL,
    relationship_type VARCHAR(50) NOT NULL,
    relationship_strength DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_content_id) REFERENCES content_classification(content_id),
    FOREIGN KEY (target_content_id) REFERENCES content_classification(content_id)
);

-- Audience mapping
CREATE TABLE content_audience (
    id SERIAL PRIMARY KEY,
    content_id VARCHAR(50) NOT NULL,
    expertise_level VARCHAR(50),
    role_types TEXT[],
    departments TEXT[],
    industries TEXT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES content_classification(content_id)
);

-- Quality metrics
CREATE TABLE quality_metrics (
    id SERIAL PRIMARY KEY,
    content_id VARCHAR(50) NOT NULL,
    metric_type VARCHAR(50) NOT NULL,
    metric_value DECIMAL(5,2),
    measurement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (content_id) REFERENCES content_classification(content_id)
);

-- Create indexes for performance
CREATE INDEX idx_taxonomy_hierarchy_path ON taxonomy_hierarchy(hierarchy_path);
CREATE INDEX idx_taxonomy_parent ON taxonomy_hierarchy(parent_id);
CREATE INDEX idx_content_classification_type ON content_classification(content_type);
CREATE INDEX idx_content_tags_value ON content_tags(tag_value);
CREATE INDEX idx_content_relationships_source ON content_relationships(source_content_id);
CREATE INDEX idx_content_relationships_target ON content_relationships(target_content_id);
CREATE INDEX idx_content_metadata_quality ON content_metadata(quality_score);
CREATE INDEX idx_classification_dimensions_type ON classification_dimensions(dimension_type);

-- Full-text search indexes
CREATE INDEX idx_content_title_fts ON content_classification USING gin(to_tsvector('english', title));
CREATE INDEX idx_content_description_fts ON content_classification USING gin(to_tsvector('english', description));
```

### 3.2 Useful SQL Queries
```sql
-- 1. Get complete hierarchy path for a content item
WITH RECURSIVE hierarchy_path AS (
    SELECT 
        unique_id,
        name,
        parent_id,
        ARRAY[name] as path
    FROM taxonomy_hierarchy
    WHERE unique_id = 'BUS-MKT-DIG-2024-00123'
    
    UNION ALL
    
    SELECT 
        t.unique_id,
        t.name,
        t.parent_id,
        t.name || h.path as path
    FROM taxonomy_hierarchy t
    INNER JOIN hierarchy_path h ON t.unique_id = h.parent_id
)
SELECT array_to_string(path, ' > ') as full_path
FROM hierarchy_path
WHERE parent_id IS NULL;

-- 2. Find all content in a specific category with quality score > 80
SELECT 
    cc.content_id,
    cc.title,
    th.hierarchy_path,
    cm.quality_score
FROM content_classification cc
JOIN taxonomy_hierarchy th ON cc.taxonomy_id = th.unique_id
JOIN content_metadata cm ON cc.content_id = cm.content_id
WHERE th.level_2 = 'Marketing'
    AND cm.quality_score > 80
ORDER BY cm.quality_score DESC;

-- 3. Get content recommendations based on relationships
SELECT 
    cc.content_id,
    cc.title,
    cr.relationship_type,
    cr.relationship_strength
FROM content_classification cc
JOIN content_relationships cr ON cc.content_id = cr.target_content_id
WHERE cr.source_content_id = 'BUS-MKT-SEO-2024-00456'
    AND cr.relationship_strength > 0.7
ORDER BY cr.relationship_strength DESC
LIMIT 10;

-- 4. Analyze content distribution across dimensions
SELECT 
    cd.dimension_type,
    cd.dimension_value,
    COUNT(*) as content_count,
    AVG(cd.confidence_score) as avg_confidence
FROM classification_dimensions cd
GROUP BY cd.dimension_type, cd.dimension_value
ORDER BY cd.dimension_type, content_count DESC;

-- 5. Find content gaps in taxonomy
SELECT 
    th.unique_id,
    th.hierarchy_path,
    COUNT(cc.content_id) as content_count
FROM taxonomy_hierarchy th
LEFT JOIN content_classification cc ON th.unique_id = cc.taxonomy_id
GROUP BY th.unique_id, th.hierarchy_path
HAVING COUNT(cc.content_id) < 3
ORDER BY th.hierarchy_path;

-- 6. Tag cloud generation
SELECT 
    tag_value,
    tag_type,
    COUNT(*) as usage_count,
    AVG(relevance_score) as avg_relevance
FROM content_tags
GROUP BY tag_value, tag_type
HAVING COUNT(*) > 5
ORDER BY usage_count DESC
LIMIT 50;

-- 7. Content lifecycle analysis
SELECT 
    DATE_TRUNC('month', cm.created_date) as month,
    cc.content_type,
    COUNT(*) as content_created,
    AVG(cm.quality_score) as avg_quality
FROM content_metadata cm
JOIN content_classification cc ON cm.content_id = cc.content_id
WHERE cm.created_date > CURRENT_DATE - INTERVAL '1 year'
GROUP BY DATE_TRUNC('month', cm.created_date), cc.content_type
ORDER BY month DESC, content_created DESC;
```

---

## 4. ANALYTICS & REPORTING QUERIES

### 4.1 Content Performance Analytics
```sql
-- Content engagement and quality dashboard
CREATE VIEW content_performance_dashboard AS
SELECT 
    cc.content_id,
    cc.title,
    cc.content_type,
    cc.knowledge_depth,
    th.hierarchy_path,
    cm.quality_score,
    cm.trust_score,
    cm.word_count,
    DATE_PART('day', NOW() - cm.modified_date) as days_since_update,
    CASE 
        WHEN cm.quality_score >= 90 THEN 'Excellent'
        WHEN cm.quality_score >= 75 THEN 'Good'
        WHEN cm.quality_score >= 60 THEN 'Fair'
        ELSE 'Needs Improvement'
    END as quality_rating,
    CASE
        WHEN DATE_PART('day', NOW() - cm.modified_date) < 30 THEN 'Current'
        WHEN DATE_PART('day', NOW() - cm.modified_date) < 90 THEN 'Recent'
        WHEN DATE_PART('day', NOW() - cm.modified_date) < 180 THEN 'Aging'
        ELSE 'Outdated'
    END as freshness_status
FROM content_classification cc
JOIN taxonomy_hierarchy th ON cc.taxonomy_id = th.unique_id
JOIN content_metadata cm ON cc.content_id = cm.content_id;
```

### 4.2 Taxonomy Coverage Report
```python
def generate_taxonomy_coverage_report(connection):
    """Generate comprehensive taxonomy coverage report"""
    
    query = """
    WITH taxonomy_stats AS (
        SELECT 
            th.level_1,
            th.level_2,
            th.level_3,
            COUNT(DISTINCT cc.content_id) as content_count,
            AVG(cm.quality_score) as avg_quality,
            COUNT(DISTINCT cm.author) as author_count,
            MAX(cm.modified_date) as last_updated
        FROM taxonomy_hierarchy th
        LEFT JOIN content_classification cc ON th.unique_id = cc.taxonomy_id
        LEFT JOIN content_metadata cm ON cc.content_id = cm.content_id
        GROUP BY th.level_1, th.level_2, th.level_3
    )
    SELECT 
        level_1,
        level_2,
        level_3,
        content_count,
        ROUND(avg_quality, 2) as avg_quality,
        author_count,
        last_updated,
        CASE 
            WHEN content_count = 0 THEN 'Empty'
            WHEN content_count < 5 THEN 'Sparse'
            WHEN content_count < 20 THEN 'Moderate'
            ELSE 'Well-Covered'
        END as coverage_status
    FROM taxonomy_stats
    ORDER BY level_1, level_2, level_3;
    """
    
    df = pd.read_sql(query, connection)
    
    # Generate summary statistics
    summary = {
        'total_categories': len(df),
        'empty_categories': len(df[df['content_count'] == 0]),
        'sparse_categories': len(df[df['coverage_status'] == 'Sparse']),
        'well_covered_categories': len(df[df['coverage_status'] == 'Well-Covered']),
        'average_content_per_category': df['content_count'].mean(),
        'total_content_items': df['content_count'].sum(),
        'overall_quality_score': df['avg_quality'].mean()
    }
    
    return df, summary
```

---

## 5. AUTOMATED CLASSIFICATION ML PIPELINE

### 5.1 Content Classifier Training
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

class AutoContentClassifier:
    """
    Machine learning pipeline for automated content classification
    """
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 3))
        self.mlb = MultiLabelBinarizer()
        self.classifier = None
        
    def prepare_training_data(self, df):
        """Prepare data for training"""
        # Combine text features
        df['combined_text'] = df['title'] + ' ' + df['description'] + ' ' + df['content']
        
        # Create multi-label targets
        df['labels'] = df.apply(lambda row: [
            row['level_1'],
            row['level_2'],
            row['content_type'],
            row['knowledge_depth']
        ], axis=1)
        
        # Transform features and labels
        X = self.vectorizer.fit_transform(df['combined_text'])
        y = self.mlb.fit_transform(df['labels'])
        
        return X, y
    
    def train_classifier(self, X, y):
        """Train the multi-label classifier"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Use MultiOutputClassifier for multi-label classification
        self.classifier = MultiOutputClassifier(
            RandomForestClassifier(n_estimators=100, random_state=42)
        )
        
        self.classifier.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.classifier.predict(X_test)
        
        # Get classification report for each label
        target_names = self.mlb.classes_
        report = classification_report(y_test, y_pred, target_names=target_names)
        
        return report
    
    def classify_new_content(self, text):
        """Classify new content"""
        X = self.vectorizer.transform([text])
        y_pred = self.classifier.predict(X)
        
        # Convert predictions back to labels
        labels = self.mlb.inverse_transform(y_pred)[0]
        
        # Get prediction probabilities
        y_proba = self.classifier.predict_proba(X)
        
        # Create classification result
        result = {
            'predicted_labels': list(labels),
            'confidence_scores': {}
        }
        
        for i, label in enumerate(self.mlb.classes_):
            if hasattr(y_proba[i], 'shape'):
                result['confidence_scores'][label] = float(y_proba[i][0][1])
        
        return result
    
    def save_model(self, filepath):
        """Save trained model and transformers"""
        model_data = {
            'vectorizer': self.vectorizer,
            'mlb': self.mlb,
            'classifier': self.classifier
        }
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
    
    def load_model(self, filepath):
        """Load trained model and transformers"""
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        
        self.vectorizer = model_data['vectorizer']
        self.mlb = model_data['mlb']
        self.classifier = model_data['classifier']

# Usage example
if __name__ == "__main__":
    # Load training data
    df = pd.read_csv('training_content.csv')
    
    # Initialize and train classifier
    auto_classifier = AutoContentClassifier()
    X, y = auto_classifier.prepare_training_data(df)
    report = auto_classifier.train_classifier(X, y)
    print("Classification Report:")
    print(report)
    
    # Save model
    auto_classifier.save_model('content_classifier_model.pkl')
    
    # Classify new content
    new_content = "This article discusses advanced machine learning techniques for natural language processing..."
    classification = auto_classifier.classify_new_content(new_content)
    print("\nClassification Result:")
    print(json.dumps(classification, indent=2))
```

---

## 6. INTEGRATION WITH EXTERNAL SYSTEMS

### 6.1 API Endpoints for Classification Service
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Initialize classification system
classifier_system = ContentClassificationSystem()
auto_classifier = AutoContentClassifier()
auto_classifier.load_model('content_classifier_model.pkl')

@app.route('/api/classify', methods=['POST'])
def classify_content():
    """Classify content via API"""
    try:
        data = request.json
        
        # Manual classification with override
        if data.get('manual_classification'):
            result = classifier_system.classify_content(data)
        else:
            # Automated classification
            text = data.get('text', '') + ' ' + data.get('title', '')
            auto_result = auto_classifier.classify_new_content(text)
            
            # Merge with manual metadata if provided
            result = {
                'content_id': classifier_system.generate_content_id(
                    auto_result['predicted_labels'][0] if auto_result['predicted_labels'] else 'UNK',
                    auto_result['predicted_labels'][1] if len(auto_result['predicted_labels']) > 1 else 'UNK',
                    'UNK'
                ),
                'classification': auto_result,
                'metadata': data.get('metadata', {})
            }
        
        return jsonify({
            'status': 'success',
            'result': result
        })
        
    except Exception as e:
        logging.error(f"Classification error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/taxonomy/search', methods=['GET'])
def search_taxonomy():
    """Search taxonomy hierarchy"""
    query = request.args.get('q', '')
    level = request.args.get('level', None)
    
    # Implement search logic here
    results = []  # Placeholder for search results
    
    return jsonify({
        'query': query,
        'results': results
    })

@app.route('/api/taxonomy/export', methods=['GET'])
def export_taxonomy():
    """Export taxonomy in various formats"""
    format_type = request.args.get('format', 'tsv')
    
    if format_type == 'tsv':
        filepath = '/tmp/taxonomy_export.tsv'
        classifier_system.export_taxonomy_tsv(filepath)
        # Return file or S3 URL
        return jsonify({
            'status': 'success',
            'file': filepath
        })
    elif format_type == 'json':
        return jsonify(classifier_system.taxonomy)
    else:
        return jsonify({'error': 'Unsupported format'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## 7. VALIDATION & QUALITY ASSURANCE

### 7.1 Taxonomy Validation Rules
```python
class TaxonomyValidator:
    """Validate taxonomy structure and content classification"""
    
    def __init__(self):
        self.validation_rules = {
            'hierarchy_depth': (1, 6),
            'name_length': (3, 255),
            'id_pattern': r'^[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-\d{4}-\d{5}$',
            'required_metadata': ['title', 'created_date', 'content_type'],
            'quality_threshold': 60.0
        }
    
    def validate_hierarchy(self, taxonomy_item):
        """Validate taxonomy hierarchy structure"""
        errors = []
        warnings = []
        
        # Check hierarchy depth
        hierarchy_levels = [taxonomy_item.get(f'level_{i}') 
                          for i in range(1, 7) 
                          if taxonomy_item.get(f'level_{i}')]
        
        if len(hierarchy_levels) < self.validation_rules['hierarchy_depth'][0]:
            errors.append("Hierarchy too shallow - minimum 1 level required")
        
        if len(hierarchy_levels) > self.validation_rules['hierarchy_depth'][1]:
            warnings.append("Hierarchy exceeds recommended depth of 6 levels")
        
        # Check naming conventions
        for level in hierarchy_levels:
            if len(level) < self.validation_rules['name_length'][0]:
                errors.append(f"Name too short: '{level}'")
            if len(level) > self.validation_rules['name_length'][1]:
                warnings.append(f"Name too long: '{level}'")
        
        # Check for duplicates in hierarchy
        if len(hierarchy_levels) != len(set(hierarchy_levels)):
            errors.append("Duplicate names in hierarchy path")
        
        return {'errors': errors, 'warnings': warnings, 'valid': len(errors) == 0}
    
    def validate_classification(self, classification):
        """Validate content classification"""
        errors = []
        warnings = []
        
        # Check required metadata
        for field in self.validation_rules['required_metadata']:
            if field not in classification or not classification[field]:
                errors.append(f"Missing required field: {field}")
        
        # Validate content ID format
        import re
        content_id = classification.get('content_id', '')
        if not re.match(self.validation_rules['id_pattern'], content_id):
            errors.append(f"Invalid content ID format: {content_id}")
        
        # Check quality score
        quality_score = classification.get('quality_score', 0)
        if quality_score < self.validation_rules['quality_threshold']:
            warnings.append(f"Quality score below threshold: {quality_score}")
        
        # Validate dimensions
        valid_content_types = ['conceptual', 'methodological', 'technical', 
                              'operational', 'tactical']
        content_type = classification.get('content_type', '')
        if content_type and content_type not in valid_content_types:
            errors.append(f"Invalid content type: {content_type}")
        
        return {'errors': errors, 'warnings': warnings, 'valid': len(errors) == 0}
    
    def batch_validate(self, df):
        """Validate entire taxonomy dataset"""
        validation_results = {
            'total_items': len(df),
            'valid_items': 0,
            'invalid_items': 0,
            'warnings_count': 0,
            'common_errors': {},
            'validation_details': []
        }
        
        for idx, row in df.iterrows():
            # Validate hierarchy
            hierarchy_result = self.validate_hierarchy(row.to_dict())
            
            # Track results
            if hierarchy_result['valid']:
                validation_results['valid_items'] += 1
            else:
                validation_results['invalid_items'] += 1
                
                # Track common errors
                for error in hierarchy_result['errors']:
                    error_type = error.split(':')[0]
                    if error_type not in validation_results['common_errors']:
                        validation_results['common_errors'][error_type] = 0
                    validation_results['common_errors'][error_type] += 1
            
            if hierarchy_result['warnings']:
                validation_results['warnings_count'] += len(hierarchy_result['warnings'])
            
            # Store detailed results for first 100 items
            if idx < 100:
                validation_results['validation_details'].append({
                    'row_index': idx,
                    'content_id': row.get('unique_id', 'N/A'),
                    'result': hierarchy_result
                })
        
        return validation_results

# Usage
validator = TaxonomyValidator()
df = pd.read_csv('taxonomy_data.tsv', sep='\t')
results = validator.batch_validate(df)
print(json.dumps(results, indent=2))
```

---

*This implementation guide provides practical templates, code examples, and SQL schemas that can be directly used to implement the comprehensive content categorization framework. The modular design allows for customization based on specific organizational needs while maintaining consistency and scalability.*
